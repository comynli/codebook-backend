import io
from datetime import datetime
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from kubernetes import client, config
from user.models import AuditModelMixin


class Project(AuditModelMixin, models.Model):
    name = models.CharField(max_length=32, validators=[RegexValidator(regex=r'^[a-z0-9-]+$')])
    description = models.CharField(max_length=255)
    members = models.ManyToManyField(User, through='ProjectMember')
    deleted_at = models.DateTimeField(default=datetime.fromtimestamp(0))

    class Meta:
        unique_together = [["name", "deleted_at"], ]


class ProjectMemberRole(models.IntegerChoices):
    GENERAL = 0, "General"
    MAINTAINER = 1, "Maintainer"
    GUEST = 2, "Guest"


class ProjectMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    role = models.IntegerField(choices=ProjectMemberRole.choices, default=ProjectMemberRole.GENERAL)

    class Meta:
        unique_together = [["user", "project"]]


class BuildSetting(AuditModelMixin, models.Model):
    project = models.OneToOneField(Project, on_delete=models.PROTECT)
    repository = models.URLField(max_length=255)
    dockerfile_path = models.CharField(max_length=255, default="Dockerfile")
    cpu_limit = models.PositiveBigIntegerField(default=2000)
    memory_limit = models.PositiveBigIntegerField(default=4000)
    cpu_request = models.PositiveBigIntegerField(default=1000)
    memory_request = models.PositiveBigIntegerField(default=2000)
    active_deadline = models.PositiveIntegerField(default=3600)


class TaskState(models.IntegerChoices):
    PENDING = 0, 'PENDING'
    RUNNING = 1, 'RUNNING'
    COMPLETED = 2, 'COMPLETED'
    FAILED = 3, 'FAILED'
    CANCELED = 4, 'CANCELED'
    TIMEOUT = 5, 'TIMEOUT'
    CANCELING = 6, 'CANCELING'


class Commit(models.Model):
    sha = models.CharField(max_length=40, unique=True)
    url = models.URLField(max_length=255)
    message = models.TextField()
    committer_name = models.CharField(max_length=64)
    committer_email = models.CharField(max_length=64)
    committed_at = models.DateTimeField()


class BuildTask(AuditModelMixin, models.Model):
    finalized = {TaskState.COMPLETED, TaskState.FAILED, TaskState.CANCELED, TaskState.TIMEOUT}

    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    state = models.IntegerField(choices=TaskState.choices, default=TaskState.PENDING)
    version = models.CharField(max_length=128)
    commit_sha = models.CharField(max_length=40)
    commit = models.ForeignKey(Commit, null=True, on_delete=models.PROTECT)
    yaml = models.TextField(null=True)
    log = models.TextField(null=True)
    uid = models.UUIDField(null=True)

    class Meta:
        unique_together = [["project", "version"]]


class Stage(AuditModelMixin, models.Model):
    name = models.CharField(max_length=32, validators=[RegexValidator(regex=r'^[a-z0-9-]+$')])
    index = models.IntegerField(default=0, unique=True)
    strict = models.BooleanField(default=False)

    class Meta:
        ordering = ["index", "-created_at"]


class Lane(AuditModelMixin, models.Model):
    name = models.CharField(max_length=32, validators=[RegexValidator(regex=r'^[a-z0-9-]+$')])
    stage = models.ForeignKey(Stage, on_delete=models.PROTECT)
    index = models.IntegerField(default=0)

    class Meta:
        unique_together = [["stage", "name"], ["stage", "index"]]
        ordering = ["index", "-created_at"]


class Cluster(AuditModelMixin, models.Model):
    name = models.CharField(max_length=32, validators=[RegexValidator(regex=r'^[a-z0-9-]+$')])
    description = models.CharField(max_length=255)
    config = models.TextField()
    registry = models.CharField(max_length=255)

    @property
    def namespace_set(self):
        config.load_kube_config(io.StringIO(self.config))
        res: client.V1NamespaceList = client.CoreV1Api().list_namespace()
        for item in res.items:
            if item.metadata.name.startswith("ingress-"):
                continue
            if item.metadata.name.startswith("kube-"):
                continue
            yield item.metadata.name


class DeploymentUnit(AuditModelMixin, models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    name = models.CharField(max_length=30, validators=[RegexValidator(regex=r'^[a-z0-9-]+$')])
    stage = models.ForeignKey(Stage, on_delete=models.PROTECT)
    lane = models.ForeignKey(Lane, on_delete=models.PROTECT)
    cluster = models.ForeignKey(Cluster, on_delete=models.PROTECT)
    namespace = models.CharField(max_length=32, validators=[RegexValidator(regex=r'^[a-z0-9-]+$')])
    template = models.TextField(null=True)
    replicas = models.IntegerField(default=1)
    cpu_limit = models.PositiveBigIntegerField(default=2000)
    memory_limit = models.PositiveBigIntegerField(default=4000)
    cpu_request = models.PositiveBigIntegerField(default=1000)
    memory_request = models.PositiveBigIntegerField(default=2000)
    progress_deadline = models.PositiveBigIntegerField(default=600)

    class Meta:
        unique_together = [
            ["project", "cluster", "namespace"],
            ["project", "lane"]
        ]


class Pipeline(AuditModelMixin, models.Model):
    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    version = models.CharField(max_length=128)
    closed = models.BooleanField(default=False)
    current = models.ForeignKey('DeployTask', on_delete=models.PROTECT, null=True, related_name="+")

    class Meta:
        ordering = ["-created_at"]


class DeployTask(AuditModelMixin, models.Model):
    finalized = {TaskState.COMPLETED, TaskState.FAILED, TaskState.CANCELED, TaskState.TIMEOUT}

    deployment_unit = models.ForeignKey(DeploymentUnit, on_delete=models.PROTECT)
    version = models.CharField(max_length=128)
    state = models.IntegerField(choices=TaskState.choices, default=TaskState.PENDING)
    yaml = models.TextField(null=True)
    error = models.TextField(null=True)
    generation = models.IntegerField(default=0)
    pipeline = models.ForeignKey(Pipeline, on_delete=models.PROTECT, null=True, related_name="+")

    class Meta:
        ordering = ["-created_at", "-generation"]
