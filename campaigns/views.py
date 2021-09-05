from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from rules.contrib.views import LoginRequiredMixin
from tenant_users.tenants.tasks import provision_tenant

from campaigns.forms import CampaignForm
from campaigns.models import Campaign
from users.models import TenantUser
from utils.mixin import PartOfTenantRequiredMixin


class CampaignListView(LoginRequiredMixin, generic.ListView):
    template_name = "campaigns/campaign_overview.html"
    model = Campaign
    context_object_name = "campaigns"

    def get_queryset(self):
        current_user: TenantUser = self.request.user
        return current_user.tenants.exclude(id=1)


class CampaignCreateView(LoginRequiredMixin, generic.FormView):
    template_name = "campaigns/campaign_edit.html"
    form_class = CampaignForm

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        slug = slugify(name).replace("-", "")
        print(slug)
        user = self.request.user
        fqdn = provision_tenant(name, slug, user.email, is_staff=True)
        return redirect("http://" + fqdn)


class CampaignDetailView(PartOfTenantRequiredMixin,LoginRequiredMixin, generic.DetailView):
    template_name = "campaigns/campaign_detail.html"
    model = Campaign
    slug_url_kwarg = "campslug"

    def get_object(self, queryset=None):
        return self.request.tenant


class CampaignEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "campaigns/campaign_edit.html"
    model = Campaign
    fields = ["name"]
    slug_url_kwarg = "campslug"

    def get_object(self, queryset=None):
        return self.request.tenant


class CampaignDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    broken at the moment
    """
    template_name = "campaigns/campaign_confirm_delete.html"
    model = Campaign
    slug_url_kwarg = "campslug"
    success_url = reverse_lazy('campaigndetail')

    def get_object(self, queryset=None):
        return self.request.tenant

    def delete(self, request, *args, **kwargs):
        self.object: Campaign = self.get_object()
        self.object.delete_tenant()
        return redirect("http://test.localhost:8000/")
