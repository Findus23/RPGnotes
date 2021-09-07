from subprocess import run

from django import template
from django.core.cache import cache

register = template.Library()


@register.simple_tag
def commit_id():
    commit = cache.get("commit")
    if not commit:
        sp = run(["git", "rev-parse", "--verify", "HEAD"], capture_output=True)
        commit = sp.stdout.decode().strip()
        cache.set("commit", commit)
    return commit
