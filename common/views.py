import json

from django.http import HttpResponse, HttpRequest, HttpResponseBadRequest, JsonResponse
from django.shortcuts import render
from django.views.decorators.http import condition
from django.views.generic import TemplateView
from ipware import get_client_ip
from sentry_sdk import last_event_id

from characters.models import Character
from common.models import Draft
from factions.models import Faction
from locations.models import Location
from loot.models import Loot
from notes.models import Note
from rpg_notes.secrets import SENTRY_DSN
from utils.assets import get_css, get_file_hash


class PublicHomepageView(TemplateView):
    template_name = "common/homepage.jinja"


class LanguageSelectView(TemplateView):
    template_name = "common/languageselect.jinja"


def print_ip(request: HttpRequest) -> HttpResponse:
    client_ip, is_routable = get_client_ip(request)
    return HttpResponse(repr(client_ip), content_type="text/plain")


def calc_etag(*args, **kwargs):
    return get_file_hash()[:6]


def save_draft(request: HttpRequest) -> HttpResponse:
    body = json.loads(request.body)
    draft_md = body.get("draft_md", None)
    if draft_md is None:
        return HttpResponseBadRequest()
    try:
        last_draft = Draft.objects.filter(author=request.user).latest()
        if last_draft.description_md == draft_md:
            return JsonResponse({
                "message": "saved (unchanged)"
            })
    except Draft.DoesNotExist:
        pass
    draft = Draft()
    draft.description_md = draft_md
    draft.author = request.user
    draft.save()
    return JsonResponse({
        "message": "saved"
    })


def name_completions(request: HttpRequest) -> HttpResponse:
    response_data = []

    for obj in (list(Location.objects.all()) +
                list(Note.objects.all()) +
                list(Faction.objects.all()) +
                list(Loot.objects.all())):
        response_data.append({
            "name": obj.name
        })
        if obj.aliases:
            for alias in obj.aliases:
                response_data.append({
                    "name": alias,
                    "details":obj.name
                })
    for char in Character.objects.all():
        response_data.append({
            "name": char.name,
            "details": char.subtitle
        })
        if char.aliases:
            for alias in char.aliases:
                response_data.append({
                    "name": alias,
                    "details":char.name
                })


    response = JsonResponse({
        "suggestions": response_data
    })
    response['Cache-Control'] = f'max-age={24 * 60 * 60}'
    return response


@condition(etag_func=calc_etag)
def debug_css(request: HttpRequest) -> HttpResponse:
    css, source_map = get_css(debug=True)
    return HttpResponse(css, content_type="text/css")


@condition(etag_func=calc_etag)
def debug_css_sourcemap(request: HttpRequest) -> HttpResponse:
    css, source_map = get_css(debug=True)
    return HttpResponse(source_map, content_type="application/json")


def handler500(request, *args, **argv):
    return render(request, "500.jinja", {
        "sentry_event_id": last_event_id(),
        "sentry_dsn": SENTRY_DSN
    }, status=500)
