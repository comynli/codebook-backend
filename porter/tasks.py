from datetime import datetime, timedelta
from django.conf import settings
from celery import shared_task
from .models import BuildTask, TaskState, DeployTask
from .runner.build import BuildRunner
from .runner.deploy import DeployRunner


@shared_task
def submit_build_task(pk):
    running = BuildTask.objects.filter(state=TaskState.RUNNING).count()
    if running < settings.BUILD_TASK_PARALLEL_NUM:
        task = BuildTask.objects.get(pk=pk)
        BuildRunner(task).submit()


@shared_task
def cancel_build_task(pk):
    task = BuildTask.objects.get(pk=pk)
    BuildRunner(task).cancel()


@shared_task
def schedule_build_task():
    running = BuildTask.objects.filter(state=TaskState.RUNNING).count()
    queryset = BuildTask.objects.filter(state=TaskState.PENDING).order_by("created_at").all()
    for task in queryset[:settings.BUILD_TASK_PARALLEL_NUM - running]:
        submit_build_task.delay(task.id)
    for task in BuildTask.objects.filter(state=TaskState.CANCELING).all():
        cancel_build_task.delay(task.id)


@shared_task
def check_deploy_task(pk):
    task = DeployTask.objects.get(pk=pk)
    DeployRunner(task).check()


@shared_task
def submit_deploy_task(pk):
    task = DeployTask.objects.get(pk=pk)
    DeployRunner(task).submit()
    eta = datetime.utcnow() + timedelta(seconds=task.deployment_unit.progress_deadline)
    check_deploy_task.apply_async((pk,), eta=eta)
