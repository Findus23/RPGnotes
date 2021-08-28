from django.urls import path

from notes import views

urlpatterns = [
    # path("", views.CampaignListView.as_view(), name="campaignlist"),
    # path("c/add", views.CampaignCreateView.as_view(), name="campaigncreate"),
    # path("c/<slug:campslug>", views.CampaignDetailView.as_view(), name="campaigndetail"),
    # path("c/<slug:campslug>/edit", views.CampaignEditView.as_view(), name="campaignedit"),
    # path("c/<slug:campslug>/delete", views.CampaignDeleteView.as_view(), name="campaigndelete"),
    path("loot", views.LootListView.as_view(), name="lootlist"),
    path("loot/<int:pk>/edit", views.LootEditView.as_view(), name="lootedit"),
    path("loot/<int:pk>/delete", views.LootDeleteView.as_view(), name="lootdelete"),
    path("loot/add", views.LootCreateView.as_view(), name="lootadd"),
    path("character/", views.list_character_redirect, name="characterlist"),
    path("character/add", views.CharacterCreateView.as_view(), name="characteradd"),
    path("character/<slug:slug>", views.CharacterDetailView.as_view(), name="characterdetail"),
    path("character/<slug:slug>/edit", views.CharacterEditView.as_view(), name="characteredit"),
    path("character/<slug:slug>/delete", views.CharacterDeleteView.as_view(), name="characterdelete"),
    path("day/", views.list_day_redirect, name="daylist"),
    path("day/add", views.DayCreateView.as_view(), name="dayadd"),
    path("day/<int:day>", views.DayDetailView.as_view(), name="daydetail"),
    path("day/<int:day>/edit", views.DayEditView.as_view(), name="dayedit"),
    path("day/<int:day>/delete", views.DayDeleteView.as_view(), name="daydelete"),
]
