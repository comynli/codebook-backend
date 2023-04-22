from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import AuthorizationViewSet, UserViewSet

router = DefaultRouter()
router.register("auth", AuthorizationViewSet, basename='auth')
router.register("", UserViewSet, basename="user")

urlpatterns = [
    path('', include(router.urls)),
]
