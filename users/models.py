from django.db import models

from tenant_users.tenants.models import UserProfile


class TenantUser(UserProfile):
    name = models.CharField(
        "Name",
        max_length=100,
        blank=True,
    )
