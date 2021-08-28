from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from notes.forms import DayForm
from notes.models import Session, Campaign, IngameDay


def list_day_redirect(request, *args, **kwargs):
    latest_day: IngameDay = IngameDay.objects.first()
    return redirect(latest_day)


class DayDetailView(generic.DetailView):
    template_name = "notes/day_detail.html"
    model = IngameDay
    context_object_name = "day"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["days"] = IngameDay.objects.filter(campaign__slug=self.kwargs['campslug'])
        return data

    def get_object(self, queryset=None):
        return IngameDay.objects.get(campaign__slug=self.kwargs['campslug'], day=self.kwargs['day'])


class DayCreateView(generic.CreateView):
    template_name = "notes/loot_edit.html"
    model = IngameDay
    form_class = DayForm
    context_object_name = "object"

    def form_valid(self, form):
        form.instance.campaign = Campaign.objects.get(slug=self.kwargs['campslug'])
        return super().form_valid(form)


class DayEditView(generic.UpdateView):
    template_name = "notes/loot_edit.html"
    model = IngameDay
    form_class = DayForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data

    def get_object(self, queryset=None):
        return IngameDay.objects.get(campaign__slug=self.kwargs['campslug'], day=self.kwargs['day'])

class DayDeleteView(generic.DeleteView):
    template_name = "notes/campaign_confirm_delete.html"
    model = IngameDay
    success_url = reverse_lazy('daylist')

    def get_object(self, queryset=None):
        return IngameDay.objects.get(campaign__slug=self.kwargs['campslug'], day=self.kwargs['day'])
