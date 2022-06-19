# Create your views here.
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from locations.forms import LocationForm
from locations.models import Location
from utils.views import JSONResponseMixin


def list_location_redirect(request, *args, **kwargs):
    first_location: Location = Location.objects.first()
    if not first_location:
        return redirect("locationadd")
    return redirect(first_location)


class LocationDetailView(JSONResponseMixin, generic.DetailView):
    template_name = "locations/detail.jinja"
    model = Location
    context_object_name = "location"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["roots"] = Location.objects.with_tree_fields()
        return data


class LocationCreateView(generic.CreateView):
    template_name = "loot/edit.jinja"
    model = Location
    form_class = LocationForm
    context_object_name = "object"


class LocationEditView(generic.UpdateView):
    template_name = "loot/edit.jinja"
    model = Location
    form_class = LocationForm

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['edit'] = True
        return data


class LocationDeleteView(generic.DeleteView):
    template_name = "common/confirm_delete.jinja"
    model = Location
    success_url = reverse_lazy('locationlist')
