from django.db import models

from tenant_users.tenants.models import UserProfile


class TenantUser(UserProfile):
    name = models.CharField(
        "Name",
        max_length=100,
        blank=True,
    )

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name
