import io
import traceback

from django.conf import settings
from porter.models import DeployTask, TaskState
from porter.utils import deserialize, serialize
from kubernetes import client, config
from kubernetes.client.exceptions import ApiException


class DeployRunner:
    def __init__(self, task: DeployTask):
        self.task = task

    @property
    def apps_api(self):
        config.load_kube_config(io.StringIO(self.task.deployment_unit.cluster.config))
        return client.AppsV1Api()

    def render(self) -> client.V1Deployment:
        template = self.task.deployment_unit.template
        if not template:
            with open("./deployment.template.yaml") as r:
                template = r.read()
        obj: client.V1Deployment = deserialize(template, client.V1Deployment)
        obj.metadata.name = self.task.deployment_unit.project.name
        obj.metadata.namespace = self.task.deployment_unit.namespace
        if obj.metadata.labels is None:
            obj.metadata.labels = dict()
        obj.metadata.labels["app"] = self.task.deployment_unit.project.name
        container: client.V1Container = obj.spec.template.spec.containers[0]
        container.image = f'{self.task.deployment_unit.cluster.registry}/{settings.IMAGE_PREFIX}/{self.task.deployment_unit.project.name}:{self.task.version}'
        container.resources = client.V1ResourceRequirements(
            limits={"cpu": f'{self.task.deployment_unit.cpu_limit}m',
                    "memory": f"{self.task.deployment_unit.memory_limit}Mi"},
            requests={"cpu": f"{self.task.deployment_unit.cpu_request}m",
                      "memory": f"{self.task.deployment_unit.memory_request}Mi"}
        )
        obj.spec.template.spec.containers[0] = container
        if obj.spec.template.metadata.labels is None:
            obj.spec.template.metadata.labels = dict()
        obj.spec.template.metadata.labels["app"] = self.task.deployment_unit.project.name
        obj.spec.selector = client.V1LabelSelector(match_labels={"app": self.task.deployment_unit.project.name})
        obj.spec.replicas = self.task.deployment_unit.replicas
        return obj

    def submit(self):
        deployment_unit = self.task.deployment_unit
        obj = self.render()
        self.task.yaml = serialize(obj)
        try:
            try:
                res = self.apps_api.replace_namespaced_deployment(deployment_unit.project.name,
                                                                  deployment_unit.namespace,
                                                                  body=obj)
                self.task.state = TaskState.RUNNING
                self.task.generation = res.metadata.generation
            except ApiException as e:
                if e.status != 404:
                    raise e
                res = self.apps_api.create_namespaced_deployment(deployment_unit.namespace, body=obj)
                self.task.state = TaskState.RUNNING
                self.task.generation = res.metadata.generation
        except ApiException as e:
            self.task.state = TaskState.FAILED
            self.task.error = e.body
        except Exception:
            self.task.state = TaskState.FAILED
            self.task.error = traceback.format_exc()
        finally:
            self.task.save()

    def check(self):
        unit = self.task.deployment_unit
        if self.task.state in DeployTask.finalized:
            return

        res = self.apps_api.read_namespaced_deployment_status(unit.project.name, unit.namespace)
        generation = res.status.observed_generation
        ready_replicas = res.status.ready_replicas
        updated_replicas = res.status.updated_replicas
        unavailable_replicas = res.status.unavailable_replicas

        if generation >= self.task.generation and unavailable_replicas is not None:
            self.task.state = TaskState.TIMEOUT
            self.task.save()
            return

        if generation >= self.task.generation and \
                ready_replicas >= unit.replicas and \
                updated_replicas is not None and \
                updated_replicas >= unit.replicas:
            self.task.state = TaskState.COMPLETED
        else:
            self.task.state = TaskState.TIMEOUT
        self.task.save()
