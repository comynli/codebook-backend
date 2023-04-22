import uuid
from abc import ABC
from datetime import timedelta
from django.utils import timezone
from django.contrib.auth import authenticate, models
from rest_framework.serializers import ModelSerializer, CharField, DateTimeField, Serializer
from rest_framework.exceptions import ValidationError
from .models import Authorization


class UserSerializer(ModelSerializer):
    class Meta:
        model = models.User
        exclude = ['password']


class UserSummarySerializer(ModelSerializer):
    class Meta:
        model = models.User
        fields = ['id', "username", "email"]


class AuthorizationSerializer(ModelSerializer):
    username = CharField(required=True, write_only=True)
    password = CharField(required=True, write_only=True)
    token = CharField(read_only=True)
    user = UserSerializer(read_only=True)
    expired_at = DateTimeField(read_only=True)

    def is_valid(self, *, raise_exception=False):
        super(AuthorizationSerializer, self).is_valid(raise_exception=raise_exception)
        user = authenticate(username=self.validated_data.pop('username'), password=self.validated_data.pop('password'))
        if user is None:
            if raise_exception:
                raise ValidationError(code=401)
            return False
        self.validated_data['token'] = uuid.uuid4().hex
        self.validated_data['user'] = user
        self.validated_data['expired_at'] = timezone.now() + timedelta(days=1)
        return True

    class Meta:
        model = Authorization
        fields = '__all__'


class AuditSerializerMixin(Serializer):
    created_at = DateTimeField(read_only=True)
    created_by = UserSummarySerializer(read_only=True)
    updated_at = DateTimeField(read_only=True)
    updated_by = UserSummarySerializer(read_only=True)
