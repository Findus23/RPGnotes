from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from days.forms import DayForm, SessionForm
from days.models import IngameDay, Session


def list_day_redirect(request, *args, **kwargs):
    latest_day: IngameDay = IngameDay.objects.first()
    if not latest_day:
        return redirect("dayadd")
    return redirect(latest_day)


class DayDetailView(generic.DetailView):
    template_name = "days/day_detail.jinja"
    model = IngameDay
    context_object_name = "day"

    def get_object(self, queryset=None):
        return IngameDay.objects.get(day=self.kwargs['day'])

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["days"] = IngameDay.objects.all().select_related()
        return data


class DayCreateView(generic.CreateView):
    template_name = "loot/edit.jinja"
    model = IngameDay
    form_class = DayForm
    context_object_name = "object"


class SessionCreateView(generic.CreateView):
    template_name = "loot/edit.jinja"
    model = Session
    form_class = SessionForm
    context_object_name = "object"
    success_url = reverse_lazy("daylist")


class DayEditView(generic.UpdateView):
    template_name = "loot/edit.jinja"
    model = IngameDay
    form_class = DayForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data

    def get_object(self, queryset=None):
        return IngameDay.objects.get(day=self.kwargs['day'])



class DayDeleteView(generic.DeleteView):
    template_name = "common/confirm_delete.jinja"
    model = IngameDay
    success_url = reverse_lazy('daylist')

    def get_object(self, queryset=None):
        return IngameDay.objects.get(day=self.kwargs['day'])
