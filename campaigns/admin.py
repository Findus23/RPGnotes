from django.contrib import admin
from django_tenants.admin import TenantAdminMixin

from campaigns.models import Campaign


@admin.register(Campaign)
class ClientAdmin(TenantAdminMixin, admin.ModelAdmin):
    list_display = ('name',)
