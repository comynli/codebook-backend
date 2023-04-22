from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import ProjectViewSet, StageViewSet, ClusterViewSet
from .consumers import BuildTaskConsumer

router = DefaultRouter()
router.register("project", ProjectViewSet, basename='project')
router.register("stage", StageViewSet, basename="stage")
router.register("cluster", ClusterViewSet, basename="cluster")

urlpatterns = [
    path('', include(router.urls)),
]

websocket_urlpatterns = [
    re_path(r"ws/porter/build/(?P<id>\d+)/$", BuildTaskConsumer.as_asgi()),
]
