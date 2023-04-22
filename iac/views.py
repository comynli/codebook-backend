from django.db.models import Q
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiTypes
from .serializers import *
from .models import Repository, Task, RunnerEvent, PeriodicTask
from .tasks import execute


class RepositoryViewSet(GenericViewSet):
    queryset = Repository.objects.all()
    serializer_class = RepositorySerializer

    @extend_schema("createRepository")
    def create(self, request: Request, *args, **kwargs):
        serializer = RepositorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, updated_by=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listRepositories", parameters=[OpenApiParameter(name='kw')])
    def list(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset()
        kw = request.query_params.get('kw')
        if kw:
            queryset = queryset.filter(name__icontains=kw)
        queryset = self.paginate_queryset(queryset)
        serializer = RepositorySerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("getRepository")
    def retrieve(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        serializer = RepositorySerializer(instance=obj)
        return Response(data=serializer.data)

    @extend_schema("updateRepository", request=RepositoryMutationSerializer)
    def update(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        serializer = RepositoryMutationSerializer(instance=obj, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("removeRepository")
    def destroy(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskViewSet(GenericViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    runner = None

    @extend_schema("execute", request=ExecuteSerializer)
    def create(self, request: Request, *args, **kwargs):
        serializer = ExecuteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, updated_by=request.user)
            # runner = AnsibleRunner(serializer.instance)
            # runner.execute()
            # self.runner.execute(serializer.instance)
            execute.delay(serializer.instance.id)
            return Response(data=TaskSerializer(instance=serializer.instance).data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listTasks", responses=TaskSummarySerializer(many=True))
    def list(self, request: Request, *args, **kwargs):
        queryset = self.paginate_queryset(self.get_queryset())
        serializer = TaskSummarySerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("getTask")
    def retrieve(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        serializer = TaskSerializer(instance=obj)
        return Response(data=serializer.data)

    @extend_schema("listTaskEvents",
                   responses=RunnerEventSerializer(many=True),
                   parameters=[OpenApiParameter(name='host')])
    @action(methods=['GET'], detail=True)
    def event(self, request: Request, *args, **kwargs):
        task = self.get_object()
        queryset = RunnerEvent.objects.filter(task=task)
        host = request.query_params.get('host')
        if host:
            queryset = queryset.filter(Q(host=host) | Q(remote_addr=host))
        queryset = self.paginate_queryset(queryset)
        serializer = RunnerEventSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("listAllEvents",
                   responses=RunnerEventSerializer(many=True),
                   parameters=[OpenApiParameter(name='host')])
    @action(methods=['GET'], detail=False, url_path="event/all")
    def list_all_event(self, request: Request, *args, **kwargs):
        queryset = RunnerEvent.objects.all()
        host = request.query_params.get('host')
        if host:
            queryset = queryset.filter(Q(host=host) | Q(remote_addr=host))
        queryset = self.paginate_queryset(queryset)
        serializer = RunnerEventSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)


class PeriodicTaskViewSet(GenericViewSet):
    queryset = PeriodicTask.objects.all()
    serializer_class = PeriodicTaskSerializer

    @extend_schema("listPeriodicTasks", responses=PeriodicTaskSerializer(many=True))
    def list(self, request: Request, *args, **kwargs):
        queryset = self.paginate_queryset(self.get_queryset())
        serializer = PeriodicTaskSerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)

    @extend_schema("getPeriodicTask")
    def retrieve(self, request: Request, *args, **kwargs):
        obj = self.get_object()
        serializer = PeriodicTaskSerializer(instance=obj)
        return Response(data=serializer.data)

    @extend_schema("createPeriodicTask", request=PeriodicTaskCreationSerializer)
    def create(self, request: Request, *args, **kwargs):
        serializer = PeriodicTaskCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user, updated_by=request.user)
            return Response(data=PeriodicTaskSerializer(instance=serializer.instance).data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("updatePeriodicTask", request=PeriodicTaskMutationSerializer)
    def update(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        serializer = PeriodicTaskMutationSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            serializer.save(updated_by=request.user)
            return Response(data=PeriodicTaskSerializer(instance=serializer.instance).data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema("listRelatedTasks", responses=TaskSummarySerializer(many=True))
    @action(methods=["GET"], detail=True)
    def tasks(self, request: Request, *args, **kwargs):
        instance = self.get_object()
        queryset = Task.objects.filter(periodic=instance)
        queryset = self.paginate_queryset(queryset)
        serializer = TaskSummarySerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)
