from getpass import getpass

from django.core.management.base import BaseCommand
from tenant_users.tenants.tasks import provision_tenant
from tenant_users.tenants.utils import create_public_tenant

from users.models import TenantUser


class Command(BaseCommand):
    help = 'sets up DTU'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        create_public_tenant("test.localhost", "rpgnotes_admin@lw1.at")
        password = getpass()
        TenantUser.objects.create_superuser(email="superuser@example.com", password=password, is_active=True)
        TenantUser.objects.create_user(email="test@lw1.at", password=password, is_active=True, is_staff=True)
        provision_tenant("Test Campaign", "testcampaign", "test@lw1.at", is_staff=True)

        print('Done')
