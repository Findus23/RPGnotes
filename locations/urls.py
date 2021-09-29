from django.urls import path

from locations import views

urlpatterns=[
    path("", views.list_location_redirect, name="locationlist"),
    path("add", views.LocationCreateView.as_view(), name="locationadd"),
    path("<slug:slug>", views.LocationDetailView.as_view(), name="locationdetail"),
    path("<slug:slug>/edit", views.LocationEditView.as_view(), name="locationedit"),
    path("<slug:slug>/delete", views.LocationDeleteView.as_view(), name="locationdelete"),

]
