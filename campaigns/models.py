from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from django_tenants.models import DomainMixin
from tenant_users.tenants.models import TenantBase

from rpg_notes.secrets import DEBUG
from utils.languages import full_text_languages, full_text_languages_choice


class Campaign(TenantBase):
    name = models.CharField(_("Name"), max_length=1000, unique=True)
    language = models.CharField(_("Language"), max_length=100, choices=full_text_languages_choice)

    auto_create_schema = True

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        print(self.get_primary_domain().domain)
        protocol = "http://" if DEBUG else "https://"
        return protocol + self.get_primary_domain().domain + (":8000" if DEBUG else "")


class Domain(DomainMixin):
    pass
