from django.urls import path

from notes import views

urlpatterns = [
    path("", views.CampaignListView.as_view(), name="campaignlist"),
    path("c/add", views.CampaignCreateView.as_view(), name="campaigncreate"),
    path("c/<slug:campslug>", views.CampaignDetailView.as_view(), name="campaigndetail"),
    path("c/<slug:campslug>/edit", views.CampaignEditView.as_view(), name="campaignedit"),
    path("c/<slug:campslug>/delete", views.CampaignDeleteView.as_view(), name="campaigndelete"),
    path("c/<slug:campslug>/loot", views.LootListView.as_view(), name="lootlist"),
    path("c/<slug:campslug>/loot/<int:pk>/edit", views.LootEditView.as_view(), name="lootedit"),
    path("c/<slug:campslug>/loot/<int:pk>/delete", views.LootDeleteView.as_view(), name="lootdelete"),
    path("c/<slug:campslug>/loot/add", views.LootCreateView.as_view(), name="lootadd"),
    path("c/<slug:campslug>/character/", views.list_character_redirect, name="characterlist"),
    path("c/<slug:campslug>/character/add", views.CharacterCreateView.as_view(), name="characteradd"),
    path("c/<slug:campslug>/character/<slug:charslug>", views.CharacterDetailView.as_view(), name="characterdetail"),
    path("c/<slug:campslug>/character/<slug:charslug>/edit", views.CharacterEditView.as_view(), name="characteredit"),
    path("c/<slug:campslug>/character/<slug:charslug>/delete", views.CharacterDeleteView.as_view(), name="characterdelete"),
    path("c/<slug:campslug>/day/", views.list_day_redirect, name="daylist"),
    path("c/<slug:campslug>/day/add", views.DayCreateView.as_view(), name="dayadd"),
    path("c/<slug:campslug>/day/<int:day>", views.DayDetailView.as_view(), name="daydetail"),
    path("c/<slug:campslug>/day/<int:day>/edit", views.DayEditView.as_view(), name="dayedit"),
    path("c/<slug:campslug>/day/<int:day>/delete", views.DayDeleteView.as_view(), name="daydelete"),
]
