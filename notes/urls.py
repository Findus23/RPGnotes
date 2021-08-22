from django.urls import path

from notes import views

urlpatterns = [
    path("", views.CampaignListView.as_view(), name="campaignlist"),
    path("c/add", views.CampaignCreateView.as_view(), name="campaigncreate"),
    path("c/<str:campslug>", views.CampaignDetailView.as_view(), name="campaigndetail"),
    path("c/<str:campslug>/edit", views.CampaignEditView.as_view(), name="campaignedit"),
    path("c/<str:campslug>/delete", views.CampaignDeleteView.as_view(), name="campaigndelete"),
    path("c/<str:campslug>/loot", views.LootListView.as_view(), name="lootlist"),
    path("c/<str:campslug>/loot/<int:pk>/edit", views.LootEditView.as_view(), name="lootedit"),
    path("c/<str:campslug>/loot/<int:pk>/delete", views.LootDeleteView.as_view(), name="lootdelete"),
    path("c/<str:campslug>/loot/add", views.LootCreateView.as_view(), name="lootadd"),
    path("c/<str:campslug>/character/", views.list_character_redirect, name="characterlist"),
    path("c/<str:campslug>/character/add", views.CharacterCreateView.as_view(), name="characteradd"),
    path("c/<str:campslug>/character/<str:charslug>", views.CharacterDetailView.as_view(), name="characterdetail"),
    path("c/<str:campslug>/character/<str:charslug>/edit", views.CharacterEditView.as_view(), name="characteredit"),
    path("c/<str:campslug>/character/<str:charslug>/delete", views.CharacterDeleteView.as_view(), name="characterdelete"),
]
