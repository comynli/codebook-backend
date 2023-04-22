from django.db import models
from django.contrib.auth.models import User


class Authorization(models.Model):
    token = models.CharField(max_length=32, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expired_at = models.DateTimeField()


class AuditModelMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="+")
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, related_name="+")

    class Meta:
        abstract = True
