from django.utils import translation
from django.core.management.base import BaseCommand

from pdf.utils import create_document


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        translation.activate("de")
        create_document()
        print("test")
