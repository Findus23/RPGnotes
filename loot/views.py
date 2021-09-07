from django.db.models import Sum
from django.urls import reverse_lazy
from django.views import generic

from loot.models import Loot
from loot.forms import LootForm


class LootListView(generic.ListView):
    template_name = "loot/overview.html"
    model = Loot
    context_object_name = "loot"

    # def get_queryset(self):
    #     return Loot.objects.filter(campaign__slug=self.kwargs['campslug'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['total_value'] = self.get_queryset().aggregate(Sum("value_gold"))["value_gold__sum"]
        print(data['total_value'])
        return data


# class LootDetailView(generic.DetailView):
#     template_name = "common/loot_detail.html"
#     model = Loot


class LootCreateView(generic.CreateView):
    template_name = "loot/edit.html"
    model = Loot
    form_class = LootForm

    success_url = reverse_lazy("lootlist")


class LootEditView(generic.UpdateView):
    template_name = "loot/edit.html"
    model = Loot
    form_class = LootForm
    context_object_name = "object"

    success_url = reverse_lazy("lootlist")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class LootDeleteView(generic.DeleteView):
    template_name = "common/campaign_confirm_delete.html"
    model = Loot

    success_url = reverse_lazy("lootlist")