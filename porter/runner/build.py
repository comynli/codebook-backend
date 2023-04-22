import logging
import threading
from urllib.parse import urlparse

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from kubernetes import client, config, watch
from kubernetes.client.exceptions import ApiException
from django.conf import settings

from ..consumers import BuildTaskConsumer
from ..models import BuildTask, BuildSetting, TaskState
from ..utils import deserialize, serialize
from ..serializers import BuildTaskSerializer

config.load_kube_config()
logging.basicConfig(level=logging.INFO)


@async_to_sync
async def send_event(group_name, data, close):
    channel_layer = get_channel_layer()
    payload = {
        "type": "on_event",
        "task": data,
        "close": close
    }
    await channel_layer.group_send(group_name, payload)


class BuildRunner:
    batch_api = client.BatchV1Api()
    core_api = client.CoreV1Api()

    def __init__(self, instance: BuildTask):
        self.instance = instance
        self.setting = BuildSetting.objects.get(project=instance.project)
        parsed = urlparse(self.setting.repository)
        self.clone_url = f'git@{parsed.netloc}:{parsed.path.strip("/")}'
        if not self.clone_url.endswith(".git"):
            self.clone_url = f'{self.clone_url}.git'
        self.image = f'{settings.IMAGE_REGISTRY}/{settings.IMAGE_PREFIX}/{self.instance.project.name}:{self.instance.version}'
        self.name = f'build-task-{self.instance.id}'
        self.logs = []
        self.event = threading.Event()

    def submit(self):
        with open("./build.template.yaml") as template:
            job: client.V1Job = deserialize(template.read(), client.V1Job)
            job.metadata.name = self.name
            container: client.V1Container = job.spec.template.spec.containers[0]
            container.command = [
                "/usr/local/bin/build.sh",
                self.clone_url,
                self.image
            ]
            container.env.append(client.V1EnvVar(name="COMMIT", value=self.instance.commit_sha))
            container.resources = client.V1ResourceRequirements(
                limits={"cpu": f'{self.setting.cpu_limit}m', "memory": f"{self.setting.memory_limit}Mi"},
                requests={"cpu": f"{self.setting.cpu_request}m", "memory": f"{self.setting.memory_request}Mi"}
            )
            job.spec.template.spec.containers[0] = container
            job.spec.active_deadline_seconds = self.setting.active_deadline
            job.spec.ttl_seconds_after_finished = 600
        try:
            res = self.batch_api.create_namespaced_job(namespace=settings.BUILD_TASK_NAMESPACE, body=job)
            res.metadata.managed_fields = None
            res.status = None
            self.instance.state = TaskState.RUNNING
            self.instance.uid = res.metadata.uid
            self.instance.yaml = serialize(res)
            self.instance.save()
            threading.Thread(target=self.watch_log, daemon=True).start()
        except ApiException as e:
            print(e.body)
            self.instance.state = TaskState.FAILED
            self.instance.save()

    def cancel(self):
        try:
            self.batch_api.delete_namespaced_job(self.name, settings.BUILD_TASK_NAMESPACE)
        except ApiException as e:
            pass
        self.instance.state = TaskState.CANCELED
        self.instance.save()
        self.push_event()

    def list_pods(self):
        if not self.instance.uid:
            return
        pods = self.core_api.list_namespaced_pod(settings.BUILD_TASK_NAMESPACE,
                                                 label_selector=f"controller-uid={self.instance.uid}")
        yield from pods.items

    def push_event(self):
        self.instance.log = "".join(self.logs)
        logging.info(f"log length {len(self.instance.log)}, log lines: {len(self.logs)}")
        send_event(BuildTaskConsumer.group_name(self.instance.id), BuildTaskSerializer(self.instance).data, False)

    def watch_log(self):
        while not self.event.is_set():
            for pod in self.list_pods():
                try:
                    logging.info(f"pod {pod.metadata.name}")
                    stream = self.core_api.read_namespaced_pod_log(pod.metadata.name,
                                                                   pod.metadata.namespace,
                                                                   follow=True,
                                                                   _preload_content=False).stream()
                    for line in stream:
                        self.logs.append(line.decode())
                        self.push_event()
                    self.event.set()
                except ApiException as e:
                    print(e.status)
            self.event.wait(1)
