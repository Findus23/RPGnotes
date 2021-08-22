from django.urls import reverse_lazy, reverse
from django.views import generic

from notes.forms import LootForm
from notes.models import Loot, Campaign


class LootListView(generic.ListView):
    template_name = "notes/loot_overview.html"
    model = Loot
    context_object_name = "loot"

    def get_queryset(self):
        return Loot.objects.filter(campaign__slug=self.kwargs['campslug'])


class LootDetailView(generic.DetailView):
    template_name = "notes/loot_detail.html"
    model = Loot


class LootCreateView(generic.CreateView):
    template_name = "notes/loot_edit.html"
    model = Loot
    form_class = LootForm

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(slug=self.kwargs['campslug'])
        return super().form_valid(form)

    success_url = reverse_lazy('lootlist')


class LootEditView(generic.UpdateView):
    template_name = "notes/loot_edit.html"
    model = Loot
    form_class = LootForm
    context_object_name = "object"

    def get_success_url(self):
        return reverse("lootlist", kwargs={"campslug": self.kwargs.get("campslug")})
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class LootDeleteView(generic.DeleteView):
    template_name = "notes/loot_confirm_delete.html"
    model = Loot
    success_url = reverse_lazy('lootlist')
