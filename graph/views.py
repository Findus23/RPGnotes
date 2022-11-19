from django.http import JsonResponse, HttpRequest, HttpResponse
from django.views.generic import TemplateView

from locations.models import Location
from notes.models import Note


# @dataclass
# class Node:
#
#
# class Graph:
#     def __init__(self):
#         self.nodes=

class GraphView(TemplateView):
    template_name = "graph/graph.jinja"


def get_graph(request: HttpRequest) -> HttpResponse:
    nodes = []
    edges = []
    for loc in list(Location.objects.all())+list(Note.objects.all()):
        nodes.append({
            "key": loc.graphkey,
            "attributes": {"label": loc.name}
        })
        if loc.parent:
            edges.append({
                "source": loc.graphkey,
                "target": loc.parent.graphkey
            })

    return JsonResponse({
        "attributes": {},
        "nodes": nodes,
        "edges": edges
    })
