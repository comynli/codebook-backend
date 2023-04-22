from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter

from .views import TaskViewSet, RepositoryViewSet, PeriodicTaskViewSet
from .consumers import AsyncEventConsumer

router = DefaultRouter()
router.register("repository", RepositoryViewSet, basename='repository')
router.register("task", TaskViewSet, basename='task')
router.register('periodic', PeriodicTaskViewSet, basename='periodic')

urlpatterns = [
    path('', include(router.urls)),
]

websocket_urlpatterns = [
    re_path(r"ws/iac/(?P<id>\d+)/$", AsyncEventConsumer.as_asgi()),
]
