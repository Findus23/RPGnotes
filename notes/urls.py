from django.urls import path

from notes import views

urlpatterns=[
    path("", views.list_note_redirect, name="notelist"),
    path("add", views.NoteCreateView.as_view(), name="noteadd"),
    path("<slug:slug>", views.NoteDetailView.as_view(), name="notedetail"),
    path("<slug:slug>/edit", views.NoteEditView.as_view(), name="noteedit"),
    path("<slug:slug>/delete", views.NoteDeleteView.as_view(), name="notedelete"),

]
