from django.urls import reverse_lazy
from django.views import generic

from notes.forms import CampaignForm
from notes.models import Campaign


class CampaignListView(generic.ListView):
    template_name = "notes/campaign_overview.html"
    model = Campaign
    context_object_name = "campaigns"


class CampaignDetailView(generic.DetailView):
    template_name = "notes/campaign_detail.html"
    model = Campaign
    slug_url_kwarg = "campslug"


class CampaignCreateView(generic.CreateView):
    template_name = "notes/campaign_edit.html"
    model = Campaign
    form_class = CampaignForm
    slug_url_kwarg = "campslug"


class CampaignEditView(generic.UpdateView):
    template_name = "notes/campaign_edit.html"
    model = Campaign
    form_class = CampaignForm
    slug_url_kwarg = "campslug"


class CampaignDeleteView(generic.DeleteView):
    template_name = "notes/campaign_confirm_delete.html"
    model = Campaign
    slug_url_kwarg = "campslug"
    success_url = reverse_lazy('campaignlist')
