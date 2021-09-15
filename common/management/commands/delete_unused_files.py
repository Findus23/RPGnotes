"""
based on https://github.com/akolpakov/django-unused-media/
licensed under MIT license
by  Andrey Kolpakov

but using pathlib and considering django-tenants
"""
from pathlib import Path
from typing import Set

from django.apps import apps
from django.core.management import BaseCommand
from django.core.validators import EMPTY_VALUES
from django.db.models import FileField
from django_tenants.utils import tenant_context

from campaigns.models import Campaign
from rpg_notes.settings import MEDIA_ROOT

media_root = Path(MEDIA_ROOT)


def get_file_fields():
    all_models = apps.get_models()

    fields = []

    for model in all_models:
        for field in model._meta.get_fields():
            if isinstance(field, FileField):
                fields.append(field)

    return fields


def get_used_media() -> Set[Path]:
    media = set()
    for field in get_file_fields():
        is_null = {
            f'{field.name}__isnull': True,
        }
        is_empty = {
            field.name: '',
        }

        storage = field.storage

        for value in field.model._base_manager \
                .values_list(field.name, flat=True) \
                .exclude(**is_empty).exclude(**is_null):
            if value not in EMPTY_VALUES:
                media.add(Path(storage.path(value)).resolve())

        return media


def get_all_media(schema: str) -> Set[Path]:
    media = set()
    schema_media_root = media_root / schema
    cache_dir = schema_media_root / "cache"
    for file in schema_media_root.glob("**/*"):
        if not file.is_file():
            continue
        if cache_dir in file.parents:
            continue
        media.add(file.resolve())
    return media


def remove_empty_directories():
    for path in media_root.glob("**/*"):
        if not path.is_dir():
            continue
        has_next = next(path.iterdir(), None)
        if not has_next:
            print("deleting", path.relative_to(media_root))
            path.rmdir()


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete duplicate files instead of listing them',
        )

    def handle(self, *args, **options):
        for campaign in Campaign.objects.exclude(pk=1):
            print(campaign, campaign.schema_name)
            with tenant_context(campaign):
                used = get_used_media()
                all = get_all_media(campaign.schema_name)
                unused = all - used
                for file in unused:
                    print("deleting", file.relative_to(media_root))
                    if options['delete']:
                        file.unlink()
        if options['delete']:
            remove_empty_directories()
