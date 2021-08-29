from django.urls import path

from campaigns import views

urlpatterns = [
    path("", views.CampaignListView.as_view(), name="campaignlist"),
    path("c/add", views.CampaignCreateView.as_view(), name="campaigncreate"),
]
