from django.urls import path

from campaigns import views as campaign_views

urlpatterns = [
    path("", campaign_views.CampaignDetailView.as_view(), name="campaigndetail"),
    path("edit", campaign_views.CampaignEditView.as_view(), name="campaignedit"),
    path("delete", campaign_views.CampaignDeleteView.as_view(), name="campaigndelete"),
]
