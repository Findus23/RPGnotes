from django.core.management.base import BaseCommand, CommandParser

from campaigns.models import Campaign
from users.models import TenantUser


class Command(BaseCommand):
    help = 'adds and removes users to/from campaigns'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("campaign_slug", type=str)
        parser.add_argument("user", type=str)
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument("--add", action="store_true")
        group.add_argument("--remove", action="store_true")

    def handle(self, *args, **options):
        user = TenantUser.objects.get(name=options.get("user"))
        campaign = Campaign.objects.get(slug=options.get("campaign_slug"))
        if options.get("add"):
            campaign.add_user(user)
            print(f"added {user} to {campaign}")
        else:
            campaign.remove_user(user)
            print(f"removed {user} from {campaign}")
        print("current users:")
        for cu in campaign.user_set.all():
            print(cu)

