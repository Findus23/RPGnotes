from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import mail_admins
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from tenant_users.tenants.tasks import provision_tenant

from campaigns.forms import CampaignForm
from campaigns.models import Campaign
from users.models import TenantUser


class CampaignListView(LoginRequiredMixin, generic.ListView):
    template_name = "campaigns/campaign_overview.jinja"
    model = Campaign
    context_object_name = "campaigns"

    def get_queryset(self):
        current_user: TenantUser = self.request.user
        return current_user.tenants.exclude(id=1)


class CampaignCreateView(LoginRequiredMixin, generic.FormView):
    template_name = "campaigns/campaign_edit.jinja"
    form_class = CampaignForm

    def form_valid(self, form):
        name = form.cleaned_data.get("name")
        slug = slugify(name).replace("-", "")
        print(slug)
        user: TenantUser = self.request.user
        super_user = TenantUser.objects.get(id=1)
        fqdn = provision_tenant(name, slug, super_user.email, is_staff=True)
        mail_admins(f"New Campaign created: {name}", "", fail_silently=True)
        campaign = Campaign.objects.get(name=name)
        campaign.add_user(user)
        return redirect("http://" + fqdn)


class CampaignDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "campaigns/campaign_detail.jinja"
    model = Campaign
    slug_url_kwarg = "campslug"

    def get_object(self, queryset=None) -> Campaign:
        return self.request.tenant

    def get_context_data(self, **kwargs):
        context = super(CampaignDetailView, self).get_context_data(**kwargs)
        players = self.get_object().user_set.exclude(pk__in=[1, 2])

        context["players"] = {}
        player: TenantUser
        for player in players:
            context["players"][player] = player.characters.all()
        return context


class CampaignEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "campaigns/campaign_edit.jinja"
    model = Campaign
    fields = ["name"]
    slug_url_kwarg = "campslug"

    def get_object(self, queryset=None):
        return self.request.tenant


class CampaignDeleteView(LoginRequiredMixin, generic.DeleteView):
    """
    broken at the moment
    """
    template_name = "common/confirm_delete.jinja"
    model = Campaign
    slug_url_kwarg = "campslug"
    success_url = reverse_lazy('campaigndetail')

    def get_object(self, queryset=None):
        return self.request.tenant

    def delete(self, request, *args, **kwargs):
        self.object: Campaign = self.get_object()
        self.object.delete_tenant()
        return redirect("http://test.localhost:8000/")
