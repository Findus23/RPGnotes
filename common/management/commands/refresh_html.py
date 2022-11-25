from django.core.management.base import BaseCommand
from django.db import transaction
from django_tenants.utils import tenant_context

from campaigns.models import Campaign
from characters.models import Character
from days.models import IngameDay
from factions.models import Faction
from locations.models import Location
from loot.models import Loot
from notes.models import Note
from utils.diff import print_diff_call
from utils.markdown import md_to_html
from utils.urls import name2url


class Command(BaseCommand):
    help = 'regenerate HTML from markdown (including autolinks)'

    def add_arguments(self, parser):
        parser.add_argument('--store', action='store_true')

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)

    def handle(self, *args, **options):
        store = options["store"]
        for campaign in Campaign.objects.exclude(pk=1):
            with tenant_context(campaign):
                with transaction.atomic():
                    replacements = name2url()
                    objects = list(Character.objects.all())
                    objects.extend(list(Location.objects.all()))
                    objects.extend(list(Loot.objects.all()))
                    objects.extend(list(Faction.objects.all()))
                    objects.extend(list(Note.objects.all()))
                    objects.extend(list(IngameDay.objects.all()))
                    for object in objects:
                        fresh_html, linked_objects = md_to_html(object.description_md, replacements=replacements)
                        if object.description_html != fresh_html:
                            print_diff_call(object.description_html, fresh_html, str(object))
                            if store:
                                object.description_html = fresh_html
                                object.linked_objects = ",".join(linked_objects)
                                object.save()
