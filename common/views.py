from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from ipware import get_client_ip
from sentry_sdk import last_event_id

from rpg_notes.secrets import SENTRY_DSN
from utils.assets import get_css


class PublicHomepageView(TemplateView):
    template_name = "common/homepage.html"


def print_ip(request):
    client_ip, is_routable = get_client_ip(request)
    print(repr(client_ip))
    return HttpResponse(repr(client_ip), content_type="text/plain")


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
