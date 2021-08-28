from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin

from users.models import TenantUser

admin.site.register(TenantUser)
