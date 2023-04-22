from datetime import datetime
from django.utils import timezone
from django.conf import settings
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from .serializers import *
from .models import ProjectMemberRole, TaskState
from .tasks import schedule_build_task, cancel_build_task, submit_deploy_task
from .gitea import GiteaClient
from .runner.pipeline import PipelineRunner


class ProjectViewSet(GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    gitea = GiteaClient(settings.GITEA_BASE_URL, settings.GITEA_TOKEN)

    def get_object_with_member(self, user, *required_roles: ProjectMemberRole):
        obj: Project = self.get_object()
        member = ProjectMember.objects.filter(project=obj, user=user).first()
        if not member:
            return None, status.HTTP_404_NOT_FOUND
        if required_roles and member.role not in required_roles:
            return None, status.HTTP_403_FORBIDDEN
        return obj, status.HTTP_200_OK

    @extend_schema("createProject")
    def create(self, request: Request, *args, **kwargs):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, updated_by=request.user)
            ProjectMember.objects.create(
                user=request.user,
                project=serializer.instance,
                role=ProjectMemberRole.MAINTAINER,
            )
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listProjects", parameters=[OpenApiParameter(name='kw')])
    def list(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset().filter(deleted_at=datetime.fromtimestamp(0))
        kw = request.query_params.get('kw')
        if kw:
            queryset = queryset.filter(name__icontains=kw)
        if not request.user.is_superuser:
            queryset = queryset.filter(members__user=request.user)
        queryset = self.paginate_queryset(queryset)
        serializer = ProjectSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("getProject")
    def retrieve(self, request: Request, *args, **kwargs):
        obj, code = self.get_object_with_member(request.user)
        if obj is None:
            return Response(status=code)
        serializer = ProjectSerializer(instance=obj)
        return Response(data=serializer.data)

    @extend_schema("updateProject", request=ProjectMutationSerializer)
    def update(self, request: Request, *args, **kwargs):
        obj, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if obj is None:
            return Response(status=code)
        serializer = ProjectMutationSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeProject")
    def destroy(self, request: Request, *args, **kwargs):
        obj, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if obj is None:
            return Response(status=code)
        obj.deleted_at = timezone.now()
        obj.updated_by = request.user
        obj.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema("getProjectMembers", responses=ProjectMemberSerializer(many=True))
    @action(methods=['GET'], detail=True)
    def members(self, request: Request, *args, **kwargs):
        obj, code = self.get_object_with_member(request.user)
        if obj is None:
            return Response(status=code)
        queryset = ProjectMember.objects.filter(project=obj)
        queryset = self.paginate_queryset(queryset)
        serializer = ProjectMemberSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("addProjectMembers", responses=ProjectMemberSerializer, request=ProjectMemberMutationSerializer)
    @members.mapping.post
    def add_member(self, request: Request, *args, **kwargs):
        obj, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if obj is None:
            return Response(status=code)
        instance = ProjectMember.objects.filter(user_id=request.data["user"], project=obj).first()
        serializer = ProjectMemberMutationSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save(project=obj)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeProjectMembers", responses=None,
                   parameters=[OpenApiParameter(name="user", type=OpenApiTypes.INT64, required=True)])
    @members.mapping.delete
    def remove_member(self, request: Request, *args, **kwargs):
        obj, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if obj is None:
            return Response(status=code)
        ProjectMember.objects.filter(user_id=request.query_params["user"], project=obj).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema("getBuildSetting", responses=BuildSettingSerializer)
    @action(methods=['GET'], detail=True, url_path="build/setting")
    def get_build_setting(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        setting = BuildSetting.objects.filter(project=project).get()
        serializer = BuildSettingSerializer(instance=setting)
        return Response(serializer.data)

    @extend_schema("saveBuildSetting", responses=BuildSettingSerializer, request=BuildSettingSerializer)
    @get_build_setting.mapping.post
    def save_build_setting(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if project is None:
            return Response(status=code)

        setting = BuildSetting.objects.filter(project=project).first()
        serializer = BuildSettingSerializer(instance=setting, data=request.data)
        if serializer.is_valid():
            serializer.save(project=project, created_by=request.user, updated_by=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listBuildTasks", responses=BuildTaskSerializer(many=True),
                   parameters=[OpenApiParameter("state", type=OpenApiTypes.INT, enum=TaskState.values, many=True)])
    @action(methods=["GET"], detail=True, url_path="build/task")
    def build_task(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)

        queryset = BuildTask.objects.filter(project=project)
        states = request.query_params.getlist("state", [])

        if len(states) > 0:
            queryset = queryset.filter(state__in=states)
        queryset = queryset.order_by("-created_at")
        queryset = self.paginate_queryset(queryset)
        serializer = BuildTaskSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("createBuildTask", responses=BuildTaskSerializer, request=BuildTaskCreationSerializer)
    @build_task.mapping.post
    def create_build_task(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        serializer = BuildTaskCreationSerializer(data=request.data)
        if serializer.is_valid():
            setting = BuildSetting.objects.get(project=project)
            commit = self.gitea.get_commit(setting.repository, serializer.validated_data["commit_sha"])
            commit = self.gitea.save(commit)
            serializer.validated_data["commit"] = commit
            serializer.save(project=project, created_by=request.user, updated_by=request.user)
            schedule_build_task.delay()
            return Response(BuildTaskSerializer(instance=serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("getBuildTask", responses=BuildTaskSerializer)
    @action(methods=["GET"], detail=True, url_path=r"build/task/(?P<task_id>\d+)")
    def get_build_task(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        task = BuildTask.objects.filter(project=project, pk=kwargs["task_id"]).get()
        serializer = BuildTaskSerializer(instance=task)
        return Response(serializer.data)

    @extend_schema("cancelBuildTask", responses={'200': BuildTaskSerializer})
    @get_build_task.mapping.delete
    def cancel_build_task(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        task = BuildTask.objects.filter(project=project, pk=kwargs["task_id"]).get()
        if task.state in {TaskState.PENDING, TaskState.RUNNING}:
            task.state = TaskState.CANCELING
            task.updated_by = request.user
            task.save()
            cancel_build_task.delay(task.id)
        serializer = BuildTaskSerializer(instance=task)
        return Response(serializer.data)

    @extend_schema("listProjectCommits", responses=CommitSerializer(many=True))
    @action(methods=["GET"], detail=True)
    def commit(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        setting = BuildSetting.objects.get(project=project)
        page = int(request.query_params.get("page", "1"))
        size = int(request.query_params.get("size", "20"))
        return Response(self.gitea.list_commit(setting.repository, page, size))

    @extend_schema("listDeploymentUnits", responses=DeploymentUnitSerializer(many=True))
    @action(methods=["GET"], detail=True, url_path="deployment")
    def deployment_unit(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        queryset = DeploymentUnit.objects.filter(project=project)
        queryset = self.paginate_queryset(queryset)
        serializer = DeploymentUnitSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("createDeploymentUnit", request=DeploymentUnitCreationSerializer, responses=DeploymentUnitSerializer)
    @deployment_unit.mapping.post
    def create_deployment_unit(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if project is None:
            return Response(status=code)
        serializer = DeploymentUnitMutationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(project=project, created_by=request.user, updated_by=request.user)
            return Response(DeploymentUnitSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("getDeploymentUnit", responses=DeploymentUnitSerializer)
    @action(methods=["GET"], detail=True, url_path=r"deployment/(?P<unit_id>\d+)")
    def deployment_unit_detail(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if project is None:
            return Response(status=code)
        instance = DeploymentUnit.objects.get(project=project, pk=kwargs["unit_id"])
        return Response(DeploymentUnitSerializer(instance).data)

    @extend_schema("updateDeploymentUnit", request=DeploymentUnitMutationSerializer, responses=DeploymentUnitSerializer)
    @deployment_unit_detail.mapping.put
    def update_deployment_unit(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if project is None:
            return Response(status=code)
        instance = DeploymentUnit.objects.get(pk=kwargs["unit_id"], project=project)
        serializer = DeploymentUnitCreationSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save(project=project, updated_by=request.user)
            return Response(DeploymentUnitSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeDeploymentUnit")
    @deployment_unit_detail.mapping.delete
    def remove_deployment_unit(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user, ProjectMemberRole.MAINTAINER)
        if project is None:
            return Response(status=code)
        instance = DeploymentUnit.objects.get(pk=kwargs["unit_id"], project=project)
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema("createDeployTask", request=DeployTaskCreationSerializer, responses=DeployTaskSerializer,
                   deprecated=True)
    @action(methods=["POST"], detail=True, url_path="deploy/task")
    def deploy(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        serializer = DeployTaskCreationSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data["deployment_unit"].project.id != project.id:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            serializer.save(created_by=request.user, updated_by=request.user)
            submit_deploy_task.delay(serializer.instance.id)
            return Response(DeployTaskSerializer(serializer.instance).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listDeployTasks", responses=DeployTaskSerializer(many=True),
                   parameters=[OpenApiParameter("unit", type=OpenApiTypes.INT64, required=True)])
    @deploy.mapping.get
    def list_deploy_tasks(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        unit_id = int(request.query_params["unit"])
        unit = DeploymentUnit.objects.get(project=project, pk=unit_id)
        queryset = DeployTask.objects.filter(deployment_unit=unit).all()
        queryset = self.paginate_queryset(queryset)
        return self.get_paginated_response(DeployTaskSerializer(queryset, many=True).data)

    @extend_schema("listPipelines", responses=PipelineSerializer(many=True))
    @action(methods=["GET"], detail=True)
    def pipeline(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        queryset = Pipeline.objects.filter(project=project).all()
        queryset = self.paginate_queryset(queryset)
        return self.get_paginated_response(PipelineSerializer(queryset, many=True).data)

    @extend_schema("startPipeline", request=PipelineSerializer, responses=PipelineSerializer)
    @pipeline.mapping.post
    def start_pipeline(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        serializer = PipelineSerializer(data=request.data)
        if serializer.is_valid():
            pipeline = PipelineRunner.start(project, serializer.validated_data["version"], request.user)
            return Response(PipelineSerializer(pipeline).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("getPipeline", responses=PipelineSerializer)
    @action(methods=["GET"], detail=True, url_path=r'pipeline/(?P<pipeline_id>\d+)')
    def pipeline_detail(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        instance = Pipeline.objects.get(project=project, pk=kwargs["pipeline_id"])
        return Response(PipelineSerializer(instance).data)

    @extend_schema("getPipelineNextActions", responses=DeploymentUnitSummarySerializer(many=True))
    @action(methods=["GET"], detail=True, url_path=r'pipeline/(?P<pipeline_id>\d+)/actions')
    def pipeline_next(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        instance = Pipeline.objects.get(project=project, pk=kwargs["pipeline_id"])
        units = PipelineRunner.next(instance)
        return Response({"results": DeploymentUnitSummarySerializer(units, many=True).data})

    @extend_schema("executePipeline", responses=PipelineSerializer,
                   request=None,
                   parameters=[OpenApiParameter("unit", OpenApiTypes.INT64)])
    @pipeline_detail.mapping.put
    def pipeline_execute(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        instance = Pipeline.objects.get(project=project, pk=kwargs["pipeline_id"])
        if request.query_params.get("unit"):
            instance = PipelineRunner.execute(instance, request.user, int(request.query_params.get("unit")))
        else:
            instance = PipelineRunner.execute(instance, request.user)
        return Response(PipelineSerializer(instance).data)

    @extend_schema("closePipeline", responses={200: PipelineSerializer})
    @pipeline_detail.mapping.delete
    def pipeline_close(self, request: Request, *args, **kwargs):
        project, code = self.get_object_with_member(request.user)
        if project is None:
            return Response(status=code)
        instance = Pipeline.objects.get(project=project, pk=kwargs["pipeline_id"])
        instance = PipelineRunner.close(instance, request.user)
        return Response(PipelineSerializer(instance).data)


class StageViewSet(GenericViewSet):
    serializer_class = StageSerializer
    queryset = Stage.objects.all()

    @extend_schema("createStage")
    def create(self, request: Request, *args, **kwargs):
        serializer = StageSerializer(data=request.data)
        if serializer.is_valid():
            index = 0
            s = Stage.objects.order_by("-index").first()
            if s:
                index = s.index + 1
            serializer.save(created_by=request.user, updated_by=request.user, index=index)
            Lane.objects.create(name="default", stage=serializer.instance)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listStages", parameters=[OpenApiParameter(name='kw')])
    def list(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset()
        kw = request.query_params.get('kw')
        if kw:
            queryset = queryset.filter(name__icontains=kw)
        queryset = self.paginate_queryset(queryset)
        serializer = StageSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("getStage")
    def retrieve(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        serializer = StageSerializer(instance=obj)
        return Response(data=serializer.data)

    @extend_schema("updateStage")
    def update(self, request: Request, *args, **kwargs):
        serializer = StageSerializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeStage")
    def destroy(self, request: Request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @extend_schema("createLane", request=LaneSerializer, responses=StageSerializer)
    @action(methods=["post"], detail=True)
    def lane(self, request: Request, *args, **kwargs):
        stage = self.get_object()
        serializer = LaneSerializer(data=request.data)
        if serializer.is_valid():
            index = 0
            l = Lane.objects.filter(stage=stage).order_by("-index").first()
            if l:
                index = l.index + 1
            serializer.save(stage=stage, created_by=request.user, updated_by=request.user, index=index)
            return Response(data=StageSerializer(self.get_object()).data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeLane", responses={200: StageSerializer}, parameters=[OpenApiParameter("name", required=True)])
    @lane.mapping.delete
    def delete_lane(self, request: Request, *args, **kwargs):
        stage = self.get_object()
        name = request.query_params["name"]
        if name != "default":
            Lane.objects.get(stage=stage, name=name).delete()
        return Response(data=StageSerializer(self.get_object()).data)


class ClusterViewSet(GenericViewSet):
    serializer_class = ClusterSerializer

    def get_queryset(self):
        user: User = self.request.user
        if user.has_perm("porter.view_cluster_config"):
            return Cluster.objects.all()
        return Cluster.objects.defer("config").all()

    @extend_schema("createCluster")
    def create(self, request: Request, *args, **kwargs):
        serializer = ClusterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, updated_by=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listClusters", parameters=[OpenApiParameter(name='kw')])
    def list(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset()
        kw = request.query_params.get('kw')
        if kw:
            queryset = queryset.filter(name__icontains=kw)
        queryset = self.paginate_queryset(queryset)
        serializer = ClusterSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("getCluster")
    def retrieve(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        serializer = ClusterSerializer(instance=obj)
        return Response(data=serializer.data)

    @extend_schema("updateCluster", request=ClusterMutationSerializer)
    def update(self, request: Request, *args, **kwargs):
        serializer = ClusterMutationSerializer(instance=self.get_object(), data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(data=ClusterSerializer(serializer.instance).data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeCluster")
    def destroy(self, request: Request, *args, **kwargs):
        self.get_object().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
