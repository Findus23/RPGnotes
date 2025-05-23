import random
from typing import Union

from django.db import connection
from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.generic import TemplateView

from characters.models import Character
from factions.models import Faction
from locations.models import Location
from loot.models import Loot, LootType
from notes.models import Note
from users.models import TenantUser

GraphModelEl = Union[Location, Note, Character, Faction, Loot, TenantUser, LootType]

# colors from https://github.com/mpetroff/accessible-color-cycles
color_cycle = ["#5790fc", "#f89c20", "#e42536", "#964a8b", "#9c9ca1", "#7a21dd"]
color_cycle.append("black")
object_types = [Location, Note, Character, Faction, Loot, TenantUser, LootType]


def color_for_object(obj: GraphModelEl):
    try:
        index = object_types.index(type(obj))
        return color_cycle[index]
    except ValueError:
        raise ValueError(f"No color defined for object of type {type(obj).__name__}")


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = set()

    def add_node(self, el: GraphModelEl, label: str = None):
        if label is None:
            label = el.name
        self.nodes.append({
            "key": el.graphkey,
            "attributes": {
                "label": label,
                "size": 10,
                "x": 0,
                "y": 0,
                "object_type": type(el).__name__,
                "color": color_for_object(el),
                "url": el.get_absolute_url() if hasattr(el, "get_absolute_url") else "/"
            }
        })

    def add_edge(self, source: GraphModelEl, target: GraphModelEl):
        if source == target:
            return
        self.edges.add((source.graphkey, target.graphkey))

    def add_edge_str(self, source: str, target: str):
        if source == target:
            return
        self.edges.add((source, target))

    def prune(self) -> None:
        connected_nodes = set()
        for e in self.edges:
            connected_nodes.add(e[0])
            connected_nodes.add(e[1])
        self.nodes = [n for n in self.nodes if n["key"] in connected_nodes]

    def export(self):
        edges = []
        for source, target in self.edges:
            edges.append({
                "source": source,
                "target": target
            })
        return {
            "attributes": {},
            "nodes": list(self.nodes),
            "edges": edges
        }


#
#
# class Graph:
#     def __init__(self):
#         self.nodes=

class GraphView(TemplateView):
    template_name = "graph/graph.jinja"


def get_description_links(el: GraphModelEl, g: Graph):
    if el.linked_objects:
        for lo in el.linked_objects.split(","):
            g.add_edge_str(el.graphkey, lo)


def get_graph(request: HttpRequest) -> HttpResponse:
    g = Graph()
    for loc in list(Location.objects.all()) + list(Note.objects.all()):
        g.add_node(loc)
        if loc.parent:
            g.add_edge(loc, loc.parent)
        get_description_links(loc, g)
    for faction in Faction.objects.all():
        g.add_node(faction, faction.name)
        get_description_links(faction, g)
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
        get_description_links(char, g)

    for loottype in LootType.objects.all():
        g.add_node(loottype)

    for loot in Loot.objects.all():
        g.add_node(loot)
        if loot.location:
            g.add_edge(loot, loot.location)
        if loot.owner:
            g.add_edge(loot, loot.owner)
        if loot.type:
            g.add_edge(loot, loot.type)
        get_description_links(loot, g)

    g.prune()

    return JsonResponse(g.export())
