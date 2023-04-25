from django.core.management.base import BaseCommand

from users.models import TenantUser


class Command(BaseCommand):
    help = 'List all users registered on instance'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        users = TenantUser.objects.all()
        for user in users:
            print(user)
