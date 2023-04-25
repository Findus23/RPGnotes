from django.core.management.base import BaseCommand

from campaigns.models import Campaign
from users.models import TenantUser


class Command(BaseCommand):
    help = 'List all campaigns registered on instance'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handle(self, *args, **options):
        campaigns = Campaign.objects.all()
        for campaign in campaigns:
            print(campaign,campaign.slug,campaign.schema_name)
