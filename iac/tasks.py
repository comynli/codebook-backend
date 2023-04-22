import time
from celery import shared_task
from .runner import AnsibleRunner
from .models import Task, TaskState, PeriodicTask


@shared_task(bind=True)
def add(self, x, y):
    print(dir(self))
    print(f'Request: {self.request!r}')
    print(f'self: {self!r}')
    time.sleep(30)
    return x + y


@shared_task(bind=True)
def execute(self, task_id):
    try:
        task = Task.objects.get(pk=task_id)
        if task.state != TaskState.PENDING:
            return
        if task.execute_id:
            return
        task.execute_id = self.request.id
        task.save()
        AnsibleRunner(task).execute()
    except Task.DoesNotExist:
        pass


def compensate_task(inspector, task):
    for items in inspector.query_task(task.execute_id).values():
        if items:
            return
    task.state = TaskState.PENDING
    task.execute_id = None
    task.save()
    execute.delay(task.id)


@shared_task
def compensate():
    for task in Task.objects.filter(state__in=[TaskState.RUNNING, TaskState.PENDING], execute_id__isnull=True):
        task.state = TaskState.PENDING
        task.save()
        execute.delay(task.id)


@shared_task(bind=True)
def compensate_with_execute_id(self):
    inspector = self.app.control.inspect()
    for task in Task.objects.filter(state__in=[TaskState.RUNNING, TaskState.PENDING], execute_id__isnull=False):
        compensate_task(inspector, task)


@shared_task()
def submit_periodic_task(uid):
    pt = PeriodicTask.objects.get(uid=uid)
    t = Task.objects.create(
        repository=pt.repository,
        playbook=pt.playbook,
        inventories=pt.inventories,
        envvars=pt.envvars,
        extravars=pt.extravars,
        periodic=pt
    )
    execute.delay(t.id)
