from django.urls import path

from factions import views

urlpatterns=[
    path("", views.list_faction_redirect, name="factionlist"),
    path("add", views.FactionCreateView.as_view(), name="factionadd"),
    path("<slug:slug>", views.FactionDetailView.as_view(), name="factiondetail"),
    path("<slug:slug>/edit", views.FactionEditView.as_view(), name="factionedit"),
    path("<slug:slug>/delete", views.FactionDeleteView.as_view(), name="factiondelete"),

]
