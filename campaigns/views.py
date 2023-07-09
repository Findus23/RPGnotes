from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.mail import mail_admins
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.text import slugify
from django.views import generic
from django.views.generic import TemplateView
from tenant_users.tenants.tasks import provision_tenant

from campaigns.forms import CampaignForm
from campaigns.models import Campaign
from characters.models import Character
from common.middlewares import demo_campaign_id
from common.models import Draft
from days.models import Session, IngameDay
from factions.models import Faction
from locations.models import Location
from loot.models import Loot, LootType
from notes.models import Note
from rpg_notes.settings import HOME_DOMAIN_URL
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


class CampaignDetailView(generic.DetailView):
    template_name = "campaigns/campaign_detail.jinja"
    model = Campaign
    slug_url_kwarg = "campslug"

    def get_object(self, queryset=None) -> Campaign:
        return self.request.tenant

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        players = self.object.user_set.exclude(pk__in=[1, 2])

        context["players"] = {}
        player: TenantUser
        for player in players:
            context["players"][player] = player.characters.all()

        context["is_demo"] = self.request.tenant.pk == demo_campaign_id
        return context


class CampaignEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = "campaigns/campaign_edit.jinja"
    model = Campaign
    form_class = CampaignForm
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
        return redirect(HOME_DOMAIN_URL)


class ExportHelpView(TemplateView):
    template_name = "campaigns/campaign_export.jinja"


class DraftView(LoginRequiredMixin, generic.ListView):
    template_name = "campaigns/draftview.jinja"
    model = Draft
    context_object_name = "drafts"

    def get_queryset(self):
        current_user: TenantUser = self.request.user
        if current_user.is_superuser:
            return Draft.objects.all().order_by("-created")
        return Draft.objects.filter(author=current_user).order_by("-created")


def export(request: HttpRequest) -> HttpResponse:
    models = {
        "characters": Character,
        "sessions": Session,
        "ingameday": IngameDay,
        "factions": Faction,
        "locations": Location,
        "loottype": LootType,
        "loot": Loot,
        "notes": Note,

    }
    data = {}
    for name, obj in models.items():
        data[name] = serializers.serialize("python", obj.objects.all())

    data["campaign"] = serializers.serialize("python", [request.tenant])[0]
    # return JsonResponse({"c": list(Character.objects.all().values())})
    return JsonResponse(data, safe=False)
