from django.contrib.auth.forms import UserChangeForm
from django.urls import reverse
from django_registration.forms import RegistrationFormUniqueEmail

from users.models import TenantUser


class CustomRegistrationForm(RegistrationFormUniqueEmail):
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
        print(password.help_text)
        password.help_text = password.help_text.replace("../password/", reverse("password_change"))
        print(password.help_text)
        self.fields['email'].disabled = True
        self.fields['last_login'].disabled = True
