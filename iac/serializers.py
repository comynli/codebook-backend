import json
import uuid
from rest_framework.serializers import ModelSerializer, Serializer, CharField, FileField, PrimaryKeyRelatedField
from drf_spectacular.utils import extend_schema_field
from drf_spectacular.types import OpenApiTypes
from django_celery_beat.models import CrontabSchedule
from django_celery_beat.models import PeriodicTask as CeleryPeriodicTask
from user.serializers import AuditSerializerMixin, UserSummarySerializer
from codebook.serializers import NonRequiredMixin
from .models import Repository, Task, RunnerEvent, PeriodicTask


@extend_schema_field(field=OpenApiTypes.BINARY)
class BinaryFileField(FileField):
    pass


class RepositorySerializer(AuditSerializerMixin, ModelSerializer):
    class Meta:
        model = Repository
        fields = '__all__'


class RepositoryMutationSerializer(NonRequiredMixin, RepositorySerializer):
    class Meta:
        model = Repository
        fields = '__all__'


class ExecuteSerializer(ModelSerializer):
    repository = PrimaryKeyRelatedField(required=True, queryset=Repository.objects.all())

    class Meta:
        model = Task
        fields = ['repository', 'playbook', 'inventories', 'envvars', 'extravars']


class TaskSerializer(AuditSerializerMixin, ModelSerializer):
    repository = RepositorySerializer()

    class Meta:
        model = Task
        fields = '__all__'


class TaskSummarySerializer(AuditSerializerMixin, ModelSerializer):
    repository = RepositorySerializer()

    class Meta:
        model = Task
        exclude = ['output']


class RunnerEventSerializer(ModelSerializer):
    class Meta:
        model = RunnerEvent
        fields = ["id", 'task', 'host', 'remote_addr', 'state', 'changed', 'playbook', 'play', 'task_name', 'start',
                  'end', 'duration']


class CrontabScheduleSerializer(ModelSerializer):
    class Meta:
        model = CrontabSchedule
        exclude = ['timezone']


class CeleryPeriodicTaskSerializer(ModelSerializer):
    crontab = CrontabScheduleSerializer()

    class Meta:
        model = CeleryPeriodicTask
        fields = ['crontab', "one_off", "enabled"]

    def create(self, validated_data):
        serializer = CrontabScheduleSerializer(data=validated_data["crontab"])
        if serializer.is_valid():
            serializer.save()
            validated_data["crontab"] = serializer.instance
        return super(CeleryPeriodicTaskSerializer, self).create(validated_data)


class CeleryPeriodicTaskMutationSerializer(NonRequiredMixin, ModelSerializer):
    crontab = CrontabScheduleSerializer()

    class Meta:
        model = CeleryPeriodicTask
        fields = ['crontab', "one_off", "enabled"]

    def update(self, instance, validated_data):
        crontab = validated_data.get("crontab")
        if crontab:
            serializer = CrontabScheduleSerializer(instance=instance.crontab, data=crontab)
            if serializer.is_valid():
                serializer.save()
                validated_data["crontab"] = serializer.instance
        return super(CeleryPeriodicTaskMutationSerializer, self).update(instance, validated_data)


class PeriodicTaskSerializer(ModelSerializer):
    repository = RepositorySerializer(read_only=True)
    periodic = CeleryPeriodicTaskSerializer(read_only=True)

    class Meta:
        model = PeriodicTask
        exclude = ["uid"]


class PeriodicTaskCreationSerializer(ModelSerializer):
    repository = PrimaryKeyRelatedField(required=True, queryset=Repository.objects.all())
    periodic = CeleryPeriodicTaskSerializer(required=True)

    def create(self, validated_data):
        serializer = CeleryPeriodicTaskSerializer(data=validated_data["periodic"])
        uid = uuid.uuid4().hex
        if serializer.is_valid():
            serializer.save(task='iac.tasks.submit_periodic_task', args=json.dumps([uid]), name=uid)
            validated_data["periodic"] = serializer.instance
            validated_data["uid"] = uid
        return super(PeriodicTaskCreationSerializer, self).create(validated_data)

    class Meta:
        model = PeriodicTask
        exclude = ["uid"]


class PeriodicTaskMutationSerializer(NonRequiredMixin, ModelSerializer):
    repository = PrimaryKeyRelatedField(required=True, queryset=Repository.objects.all())
    periodic = CeleryPeriodicTaskMutationSerializer()

    class Meta:
        model = PeriodicTask
        exclude = ["uid"]

    def update(self, instance, validated_data):
        serializer = CeleryPeriodicTaskMutationSerializer(instance=instance.periodic, data=validated_data["periodic"])
        if serializer.is_valid():
            serializer.save()
            validated_data["periodic"] = serializer.instance
        return super(PeriodicTaskMutationSerializer, self).update(instance, validated_data)
