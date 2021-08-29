from django.urls import path

from characters import views

urlpatterns=[
    path("", views.list_character_redirect, name="characterlist"),
    path("add", views.CharacterCreateView.as_view(), name="characteradd"),
    path("<slug:slug>", views.CharacterDetailView.as_view(), name="characterdetail"),
    path("<slug:slug>/edit", views.CharacterEditView.as_view(), name="characteredit"),
    path("<slug:slug>/delete", views.CharacterDeleteView.as_view(), name="characterdelete"),

]
