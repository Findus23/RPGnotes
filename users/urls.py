from django.urls import path
from django.views.generic.base import TemplateView

from . import views

urlpatterns = [
    path(
        "activate/<str:activation_key>/",
        views.CustomActivationView.as_view(),
        name="django_registration_activate",
    ),
    path(
        "register/",
        views.CustomRegistrationView.as_view(),
        name="django_registration_register",
    ),
    path(
        "register/closed/",
        TemplateView.as_view(
            template_name="registration/registration_closed.jinja"
        ),
        name="django_registration_disallowed",
    ),
]
