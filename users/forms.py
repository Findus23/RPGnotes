from django_registration.forms import RegistrationForm

from users.models import TenantUser


class CustomRegistrationForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = TenantUser
        fields = [
            "name",
            "email",
            "password1",
            "password2",
        ]
