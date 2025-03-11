from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_registration.forms import RegistrationFormUniqueEmail

from rpg_notes.secrets import REGISTRATION_TOKEN
from users.models import TenantUser


def validate_registration_token(user_input: str):
    if user_input != REGISTRATION_TOKEN:
        raise forms.ValidationError(_("Invalid registration token. Please contact me for the current token."))


class CustomRegistrationForm(RegistrationFormUniqueEmail):
    registration_token = forms.CharField(
        label=_("Registration Token"),
        help_text=_("Registration on this website is currently closed to the public. If you are interested in creating an account, please contact me for the current registration token."),
        validators=[validate_registration_token]
    )

    class Meta(RegistrationFormUniqueEmail.Meta):
        model = TenantUser
        fields = [
            "name",
            "email",
            "password1",
            "password2",
        ]


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = TenantUser
        fields = [
            "name",
            "password",
            "email",
            "last_login"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get('password')
        password.help_text = password.help_text.replace("../password/", reverse("password_change"))
        self.fields['email'].disabled = True
        self.fields['last_login'].disabled = True
