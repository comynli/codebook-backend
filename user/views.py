from django.contrib.auth.models import User
from rest_framework.viewsets import GenericViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.status import HTTP_401_UNAUTHORIZED, HTTP_204_NO_CONTENT
from rest_framework.permissions import AllowAny
from drf_spectacular.views import extend_schema, OpenApiParameter, OpenApiTypes
from .serializers import AuthorizationSerializer, UserSummarySerializer
from .models import Authorization


class AuthorizationViewSet(GenericViewSet):
    serializer_class = AuthorizationSerializer
    permission_classes = [AllowAny]

    @extend_schema("login")
    @action(methods=["post"], detail=False, url_path="login")
    def login(self, request: Request, *args, **kwargs):
        serializer = AuthorizationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)
        return Response(data=serializer.errors, status=HTTP_401_UNAUTHORIZED)

    @extend_schema("logout", request=None, responses=None,
                   parameters=[OpenApiParameter(name="all", type=OpenApiTypes.BOOL, default=False)])
    @action(methods=["put"], detail=False, url_path="logout")
    def logout(self, request: Request, *args, **kwargs):
        queryset = Authorization.objects.all()
        if not request.auth:
            return Response(status=HTTP_204_NO_CONTENT)
        is_all = request.query_params.get("all")
        if is_all and is_all.lower() == 'true':
            queryset = queryset.filter(user=request.user)
        else:
            queryset = queryset.filter(token=request.auth)
        queryset.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class UserViewSet(GenericViewSet):
    serializer_class = UserSummarySerializer
    queryset = User.objects.all()

    @extend_schema("listUsers", responses=UserSummarySerializer(many=True), parameters=[OpenApiParameter(name="kw")])
    def list(self, request: Request, *args, **kwargs):
        queryset = self.get_queryset()
        kw = request.query_params.get("kw")
        if kw:
            queryset = queryset.filter(username__icontains=kw)
        queryset = self.paginate_queryset(queryset)
        serializer = UserSummarySerializer(instance=queryset, many=True)
        return self.get_paginated_response(serializer.data)
