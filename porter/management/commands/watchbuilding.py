import logging
import threading

from django.conf import settings
from django.core.management.base import BaseCommand
from kubernetes import client, config
from kubernetes.watch import watch

from porter.consumers import BuildTaskConsumer
from porter.models import BuildTask, TaskState
from porter.serializers import BuildTaskSerializer
from porter.utils import serialize
from porter.runner.build import send_event
from porter.tasks import schedule_build_task

config.load_kube_config()
logging.basicConfig(level=logging.INFO)


class Command(BaseCommand):
    help = "watch build tasks"
    event = threading.Event()
    batch_api = client.BatchV1Api()
    core_api = client.CoreV1Api()

    def read_log(self, uid):
        items = []
        pods = self.core_api.list_namespaced_pod(settings.BUILD_TASK_NAMESPACE,
                                                 label_selector=f"controller-uid={uid}")
        for pod in pods.items:
            item = self.core_api.read_namespaced_pod_log(pod.metadata.name, pod.metadata.namespace)
            items.append(item)
        return '\n'.join(items)

    def watch(self):
        while not self.event.is_set():
            w = watch.Watch()
            for evt in w.stream(self.batch_api.list_namespaced_job, namespace=settings.BUILD_TASK_NAMESPACE):
                res: client.V1Job = evt["object"]
                logging.info(serialize(res.status))
                task = BuildTask.objects.filter(uid=res.metadata.uid).first()
                if not task:
                    continue

                if res.status.failed is not None or res.status.succeeded is not None:
                    task.state = TaskState.FAILED if res.status.failed is not None else TaskState.COMPLETED
                    task.log = self.read_log(res.metadata.uid)
                    task.save()
                    schedule_build_task.delay()
                    send_event(BuildTaskConsumer.group_name(task.id), BuildTaskSerializer(task).data, True)
            w.stop()
            self.event.wait(2)

    def handle(self, *args, **options):
        try:
            self.watch()
        except KeyboardInterrupt:
            self.event.set()
