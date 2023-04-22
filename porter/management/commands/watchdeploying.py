import io
import threading

import yaml
from django.core.management import BaseCommand
from kubernetes import config, client, watch
from porter.models import Cluster, DeploymentUnit, DeployTask, TaskState


def get_default(v, default):
    if v is None:
        return default
    return v


class Command(BaseCommand):
    help = "watch build tasks"
    event = threading.Event()

    @staticmethod
    def apps_api(cluster: Cluster):
        with threading.Lock():
            cfg = yaml.safe_load(cluster.config)
            api_client = config.new_client_from_config_dict(cfg)
            return client.AppsV1Api(api_client=api_client)

    def watch(self, cluster):
        apps_api = self.apps_api(cluster)
        while not self.event.is_set():
            w = watch.Watch()
            for event in w.stream(apps_api.list_deployment_for_all_namespaces):
                res: client.V1Deployment = event["object"]
                unit = DeploymentUnit.objects.filter(project__name=res.metadata.name, cluster=cluster,
                                                     namespace=res.metadata.namespace).first()
                if unit is None:
                    continue
                generation = get_default(res.status.observed_generation, 0)
                ready_replicas = get_default(res.status.ready_replicas, 0)
                updated_replicas = get_default(res.status.updated_replicas, 0)
                unavailable_replicas = res.status.unavailable_replicas
                if unavailable_replicas is not None:
                    continue
                if ready_replicas >= unit.replicas and \
                        updated_replicas >= unit.replicas:
                    DeployTask.objects.filter(deployment_unit=unit, generation__lte=generation,
                                              state__in=[TaskState.PENDING, TaskState.RUNNING]) \
                        .update(state=TaskState.COMPLETED)
            w.stop()
            self.event.wait(2)

    def handle(self, *args, **options):
        threads = []
        try:
            for cluster in Cluster.objects.all():
                t = threading.Thread(target=self.watch, args=(cluster,), daemon=True)
                t.start()
                threads.append(t)
            for t in threads:
                t.join()
        except KeyboardInterrupt:
            self.event.set()
