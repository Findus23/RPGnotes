from django.urls import path

from graph import views

urlpatterns = [
    path("", views.GraphView.as_view(), name="graph"),
]
