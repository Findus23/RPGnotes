from django.db.models import Sum
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

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(slug=self.kwargs['campslug'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("lootlist", kwargs={"campslug": self.kwargs.get("campslug")})


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
    template_name = "notes/campaign_confirm_delete.html"
    model = Loot
    def get_success_url(self):
        return reverse("lootlist", kwargs={"campslug": self.kwargs.get("campslug")})
