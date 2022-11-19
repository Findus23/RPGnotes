from typing import Union

from django.db import connection
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.generic import TemplateView

from characters.models import Character
from factions.models import Faction
from locations.models import Location
from notes.models import Note
from users.models import TenantUser

GraphModelEl = Union[Location, Note, Character, Faction]


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, el: GraphModelEl, label: str = None):
        if label is None:
            label = el.name
        self.nodes.append({
            "key": el.graphkey,
            "attributes": {
                "label": label,
                "size": 20
            }
        })

    def add_edge(self, source: GraphModelEl, target: GraphModelEl):
        self.edges.append({
            "source": source.graphkey,
            "target": target.graphkey
        })


#
#
# class Graph:
#     def __init__(self):
#         self.nodes=

class GraphView(TemplateView):
    template_name = "graph/graph.jinja"


def get_graph(request: HttpRequest) -> HttpResponse:
    g = Graph()
    for loc in list(Location.objects.all()) + list(Note.objects.all()):
        g.add_node(loc)
        if loc.parent:
            g.add_edge(loc, loc.parent)
    for faction in Faction.objects.all():
        g.add_node(faction, faction.name)
    for user in TenantUser.objects \
            .filter(tenants=connection.get_tenant()) \
            .exclude(pk__in=[1, 2]):
        g.add_node(user, user.name)

    for char in Character.objects.all():
        g.add_node(char)
        if char.location:
            g.add_edge(char, char.location)
        if char.faction:
            g.add_edge(char, char.faction)
        if char.player:
            g.add_edge(char, char.player)

    return JsonResponse({
        "attributes": {},
        "nodes": g.nodes,
        "edges": g.edges
    })
