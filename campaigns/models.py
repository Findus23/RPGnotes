from django.db import models
# Create your models here.
from django_tenants.models import DomainMixin
from tenant_users.tenants.models import TenantBase

from rpg_notes.secrets import DEBUG


class Campaign(TenantBase):
    name = models.CharField(max_length=1000)

    auto_create_schema = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print(self.get_primary_domain().domain)
        protocol = "http://" if DEBUG else "https://"
        return protocol + self.get_primary_domain().domain + (":8000" if DEBUG else "")


class Domain(DomainMixin):
    pass
