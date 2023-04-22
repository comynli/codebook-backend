from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, DateTimeField, PrimaryKeyRelatedField, ListSerializer, \
    CharField, IntegerField, SlugRelatedField
from user.serializers import UserSummarySerializer, AuditSerializerMixin
from codebook.serializers import NonRequiredMixin
from .models import Project, ProjectMember, BuildSetting, BuildTask, Commit
from .models import Stage, Lane, Cluster, DeploymentUnit, DeployTask, Pipeline


class ProjectMemberSerializer(ModelSerializer):
    user = UserSummarySerializer()

    class Meta:
        model = ProjectMember
        fields = '__all__'


class ProjectMemberMutationSerializer(ModelSerializer):
    user = PrimaryKeyRelatedField(queryset=User.objects.filter(is_active=True))

    class Meta:
        model = ProjectMember
        fields = ["user", "role"]


class ProjectSerializer(AuditSerializerMixin, ModelSerializer):
    deleted_at = DateTimeField(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class ProjectMutationSerializer(NonRequiredMixin, ProjectSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class BuildSettingSerializer(AuditSerializerMixin, ModelSerializer):
    class Meta:
        model = BuildSetting
        exclude = ["project"]


class CommitSerializer(ModelSerializer):
    class Meta:
        model = Commit
        fields = "__all__"


class BuildTaskSerializer(AuditSerializerMixin, ModelSerializer):
    commit = CommitSerializer(read_only=True)

    class Meta:
        model = BuildTask
        exclude = ["project"]
        read_only_fields = ["state", "yaml"]


class BuildTaskCreationSerializer(ModelSerializer):
    class Meta:
        model = BuildTask
        fields = ["version", "commit_sha"]


class LaneSerializer(AuditSerializerMixin, ModelSerializer):
    index = IntegerField(read_only=True)

    class Meta:
        model = Lane
        exclude = ["stage"]


class StageSerializer(AuditSerializerMixin, ModelSerializer):
    lane_set = LaneSerializer(many=True, read_only=True)
    index = IntegerField(read_only=True)

    class Meta:
        model = Stage
        fields = '__all__'


class ClusterSerializer(AuditSerializerMixin, ModelSerializer):
    namespace_set = ListSerializer(read_only=True, child=CharField())

    class Meta:
        model = Cluster
        fields = '__all__'


class ClusterMutationSerializer(NonRequiredMixin, ModelSerializer):
    class Meta:
        model = Cluster
        fields = '__all__'


class DeploymentUnitSerializer(AuditSerializerMixin, ModelSerializer):
    stage = StageSerializer(read_only=True)
    cluster = ClusterSerializer(read_only=True)
    lane = LaneSerializer(read_only=True)

    class Meta:
        model = DeploymentUnit
        fields = '__all__'


class DeploymentUnitSummarySerializer(ModelSerializer):
    stage = SlugRelatedField(slug_field="name", read_only=True)
    cluster = SlugRelatedField(slug_field="name", read_only=True)
    lane = SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = DeploymentUnit
        fields = ["id", "name", "stage", "cluster", "lane", "namespace"]


class DeploymentUnitCreationSerializer(AuditSerializerMixin, ModelSerializer):
    stage = PrimaryKeyRelatedField(queryset=Stage.objects.all())
    cluster = PrimaryKeyRelatedField(queryset=Cluster.objects.all())
    lane = PrimaryKeyRelatedField(queryset=Lane.objects.all())

    class Meta:
        model = DeploymentUnit
        exclude = ['project']


class DeploymentUnitMutationSerializer(NonRequiredMixin, DeploymentUnitCreationSerializer):
    id = IntegerField(write_only=True, required=True)

    class Meta:
        model = DeploymentUnit
        exclude = ['project']


class DeployTaskSerializer(AuditSerializerMixin, ModelSerializer):
    deployment_unit = DeploymentUnitSummarySerializer(read_only=True)

    class Meta:
        model = DeployTask
        exclude = ["pipeline"]


class PipelineSerializer(AuditSerializerMixin, ModelSerializer):
    current = DeployTaskSerializer(read_only=True)

    class Meta:
        model = Pipeline
        exclude = ['project']
        read_only_fields = ["closed"]


class DeployTaskCreationSerializer(ModelSerializer):
    deployment_unit = PrimaryKeyRelatedField(queryset=DeploymentUnit.objects.all())

    class Meta:
        model = DeployTask
        fields = ["deployment_unit", "version"]
