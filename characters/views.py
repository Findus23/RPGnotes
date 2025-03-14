from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from characters.forms import CharacterForm
from characters.models import Character
from utils.views import JSONResponseMixin


def list_character_redirect(request, *args, **kwargs):
    first_character: Character = Character.objects.first()
    if not first_character:
        return redirect("characteradd")
    return redirect(first_character)


class CharacterDetailView(JSONResponseMixin, generic.DetailView):
    template_name = "characters/detail.jinja"
    model = Character
    context_object_name = "character"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["player_characters"] = Character.objects.filter(
            player__isnull=False
        ).select_related()
        data["npcs"] = Character.objects.filter(
            player__isnull=True,
            archived=False
        ).select_related()
        data["npcs_archived"] = Character.objects.filter(
            player__isnull=True,
            archived=True
        ).select_related()
        return data



class CharacterCreateView(generic.CreateView):
    template_name = "loot/edit.jinja"
    model = Character
    form_class = CharacterForm
    context_object_name = "object"


class CharacterEditView(generic.UpdateView):
    template_name = "loot/edit.jinja"
    model = Character
    form_class = CharacterForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class CharacterDeleteView(generic.DeleteView):
    template_name = "common/confirm_delete.jinja"
    model = Character
    success_url = reverse_lazy('characterlist')
