from django.db import models
from django.contrib.auth.models import User
from django_celery_beat.models import PeriodicTask as CeleryPeriodicTask
from user.models import AuditModelMixin


class Repository(AuditModelMixin, models.Model):
    name = models.CharField(max_length=64, unique=True)
    git_url = models.CharField(max_length=256, default='')

    class Meta:
        ordering = ["name"]


class TaskState(models.IntegerChoices):
    PENDING = 0, 'PENDING'
    RUNNING = 1, 'RUNNING'
    COMPLETED = 2, 'COMPLETED'
    FAILED = 3, 'FAILED'
    CANCELED = 4, 'CANCELED'
    TIMEOUT = 5, 'TIMEOUT'
    CANCELING = 6, 'CANCELING'


class BaseTask(AuditModelMixin, models.Model):
    finalized = {TaskState.COMPLETED, TaskState.FAILED, TaskState.CANCELED, TaskState.TIMEOUT}

    repository = models.ForeignKey(Repository, on_delete=models.PROTECT)
    playbook = models.CharField(max_length=64, default="site.yml")
    inventories = models.TextField(default='', blank=True)
    envvars = models.TextField(default='', blank=True)
    extravars = models.TextField(default='', blank=True)

    class Meta:
        abstract = True


class PeriodicTask(BaseTask):
    uid = models.UUIDField(unique=True)
    periodic = models.ForeignKey(CeleryPeriodicTask, on_delete=models.PROTECT)


class Task(BaseTask):
    commit_id = models.CharField(max_length=40, default='')
    state = models.IntegerField(default=TaskState.PENDING)
    output = models.TextField(default='')
    execute_id = models.UUIDField(null=True)
    periodic = models.ForeignKey(PeriodicTask, on_delete=models.PROTECT, null=True)

    class Meta:
        ordering = ['-created_at']


class RunnerEvent(models.Model):
    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    host = models.CharField(max_length=256)
    changed = models.BooleanField(null=True)
    playbook = models.CharField(max_length=64)
    playbook_uuid = models.UUIDField()
    play = models.CharField(max_length=255)
    play_uuid = models.UUIDField()
    task_name = models.CharField(max_length=255)
    task_uuid = models.UUIDField()
    remote_addr = models.GenericIPAddressField(null=True)
    state = models.IntegerField(choices=TaskState.choices, default=TaskState.RUNNING)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    duration = models.FloatField(default=0)
    res = models.JSONField(null=True)

    class Meta:
        unique_together = [
            ['task_id', 'host', 'playbook_uuid', 'play_uuid', 'task_uuid']
        ]
