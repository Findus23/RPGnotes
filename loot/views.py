from django.db.models import Sum
from django.urls import reverse_lazy
from django.views import generic

from loot.forms import LootForm
from loot.models import Loot
from utils.views import JSONResponseMixin


class LootListView(generic.ListView):
    template_name = "loot/overview.jinja"
    model = Loot
    context_object_name = "loot"

    def get_queryset(self):
        show_former = self.request.GET.get('show_former', False) == "true"
        return Loot.objects.filter(former=show_former)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['total_value'] = self.get_queryset().aggregate(Sum("value_gold"))["value_gold__sum"]
        return data


# class LootDetailView(generic.DetailView):
#     template_name = "common/loot_detail.html"
#     model = Loot


class LootCreateView(generic.CreateView):
    template_name = "loot/edit.jinja"
    model = Loot
    form_class = LootForm

    success_url = reverse_lazy("lootlist")


class LootEditView(JSONResponseMixin, generic.UpdateView):
    template_name = "loot/edit.jinja"
    model = Loot
    form_class = LootForm
    context_object_name = "object"

    success_url = reverse_lazy("lootlist")

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class LootDeleteView(generic.DeleteView):
    template_name = "common/confirm_delete.jinja"
    model = Loot

    success_url = reverse_lazy("lootlist")
