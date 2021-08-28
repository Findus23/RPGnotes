from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import CharacterForm
from notes.models import Character, Campaign


# class CharacterListView(generic.ListView):
#     template_name = "notes/character_overview.html"
#     model = Character
#     context_object_name = "character"
#
#
#

def list_character_redirect(request, *args, **kwargs):
    first_character:Character=Character.objects.first()

    return redirect(first_character)


class CharacterDetailView(generic.DetailView):
    template_name = "notes/character_detail.html"
    model = Character
    context_object_name = "character"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["player_characters"] = Character.objects.filter(
            campaign__slug=self.kwargs['campslug'],
            player__isnull=False
        ).select_related()
        data["npcs"] = Character.objects.filter(
            campaign__slug=self.kwargs['campslug'], player__isnull=True
        ).select_related()
        return data

    def get_object(self, queryset=None):
        return Character.objects.get(
            campaign__slug=self.kwargs['campslug'], slug=self.kwargs['charslug']
        )


class CharacterCreateView(generic.CreateView):
    template_name = "notes/loot_edit.html"
    model = Character
    form_class = CharacterForm
    context_object_name = "object"

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(slug=self.kwargs['campslug'])
        return super().form_valid(form)


class CharacterEditView(generic.UpdateView):
    template_name = "notes/loot_edit.html"
    model = Character
    form_class = CharacterForm

    def get_object(self, queryset=None):
        return Character.objects.get(campaign__slug=self.kwargs['campslug'], slug=self.kwargs['charslug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class CharacterDeleteView(generic.DeleteView):
    template_name = "notes/campaign_confirm_delete.html"
    model = Character
    success_url = reverse_lazy('characterlist')
