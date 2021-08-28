from django.db.models import Sum
from django.urls import reverse_lazy, reverse
from django.views import generic

from notes.forms import LootForm
from notes.models import Loot


class LootListView(generic.ListView):
    template_name = "notes/loot_overview.html"
    model = Loot
    context_object_name = "loot"

    # def get_queryset(self):
    #     return Loot.objects.filter(campaign__slug=self.kwargs['campslug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['total_value'] = self.get_queryset().aggregate(Sum("value_gold"))["value_gold__sum"]
        print(data['total_value'])
        return data


class LootDetailView(generic.DetailView):
    template_name = "notes/loot_detail.html"
    model = Loot


class LootCreateView(generic.CreateView):
    template_name = "notes/loot_edit.html"
    model = Loot
    form_class = LootForm

    success_url = reverse_lazy("lootlist")



class LootEditView(generic.UpdateView):
    template_name = "notes/loot_edit.html"
    model = Loot
    form_class = LootForm
    context_object_name = "object"

    success_url = reverse_lazy("lootlist")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class LootDeleteView(generic.DeleteView):
    template_name = "notes/campaign_confirm_delete.html"
    model = Loot

    success_url = reverse_lazy("lootlist")
