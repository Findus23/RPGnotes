from django.urls import path

from campaigns import views as campaign_views

urlpatterns = [
    path("", campaign_views.CampaignDetailView.as_view(), name="campaigndetail"),
    path("edit", campaign_views.CampaignEditView.as_view(), name="campaignedit"),
    path("export", campaign_views.ExportHelpView.as_view(), name="export"),
    path("auto-saves", campaign_views.DraftView.as_view(), name="drafts"),
    path("export/data", campaign_views.export, name="exportdata"),
    path("delete", campaign_views.CampaignDeleteView.as_view(), name="campaigndelete"),
]
