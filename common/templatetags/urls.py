from django import template

from rpg_notes.settings import DEBUG, DOMAIN

register = template.Library()


@register.simple_tag
def main_url():
    protocol = "http" if DEBUG else "https"
    return f"{protocol}://{DOMAIN}"
