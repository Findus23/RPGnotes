from django.urls import path

from pdf import views

urlpatterns=[
    path("", views.pdf, name="document"),
]
