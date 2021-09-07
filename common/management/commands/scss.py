from django.core.management.base import BaseCommand

from utils.assets import save_css


class Command(BaseCommand):
    help = 'compile scss'

    def handle(self, *args, **kwargs):
        save_css()
