# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from factions.forms import FactionForm
from factions.models import Faction


def list_faction_redirect(request, *args, **kwargs):
    first_faction: Faction = Faction.objects.first()
    if not first_faction:
        return redirect("factionadd")
    return redirect(first_faction)


class FactionDetailView(generic.DetailView):
    template_name = "factions/detail.jinja"
    model = Faction
    context_object_name = "faction"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["factions"] = Faction.objects.all().select_related()
        return data


class FactionCreateView(generic.CreateView):
    template_name = "loot/edit.jinja"
    model = Faction
    form_class = FactionForm
    context_object_name = "object"


class FactionEditView(generic.UpdateView):
    template_name = "loot/edit.jinja"
    model = Faction
    form_class = FactionForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class FactionDeleteView(generic.DeleteView):
    template_name = "common/confirm_delete.jinja"
    model = Faction
    success_url = reverse_lazy('factionlist')
