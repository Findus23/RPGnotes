from django.http import HttpResponse
from django.shortcuts import render
from sentry_sdk import last_event_id

from rpg_notes.secrets import SENTRY_DSN
from utils.assets import get_css


# @cache_page(60 * 15)
def debug_css(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(css, content_type="text/css")


# @cache_page(60 * 15)
def debug_css_sourcemap(request):
    css, source_map = get_css(debug=True)
    return HttpResponse(source_map, content_type="application/json")


def handler500(request, *args, **argv):
    return render(request, "500.html", {
        "sentry_event_id": last_event_id(),
        "sentry_dsn": SENTRY_DSN
    }, status=500)
