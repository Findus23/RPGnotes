from django.urls import path

from campaigns import views

urlpatterns = [
    path("campaigns/", views.CampaignListView.as_view(), name="campaignlist"),
    path("campaigns/add", views.CampaignCreateView.as_view(), name="campaigncreate"),
]
