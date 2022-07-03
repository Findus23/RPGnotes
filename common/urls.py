from django.urls import path

from common import views

urlpatterns = [
    path("api/draft/save", views.save_draft, name="save_draft"),
]
