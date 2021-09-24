from django.contrib import messages
from django.core.mail import mail_admins
from django.urls import reverse_lazy
from django_registration.backends.activation.views import RegistrationView, ActivationView

from users.forms import CustomRegistrationForm
from users.models import TenantUser


class CustomRegistrationView(RegistrationView):
    email_body_template = "users/activation_email_body.html"
    email_subject_template = "users/activation_email_subject.html"
    template_name = "users/registration_form.html"
    form_class = CustomRegistrationForm
    success_url = reverse_lazy("login")

    def create_inactive_user(self, form: CustomRegistrationForm):
        """
        Create the inactive user account and send an email containing
        activation instructions.

        """
        data = form.cleaned_data
        new_user = TenantUser.objects.create_user(
            email=data.get("email"),
            password=data.get("password1"),
            name=data.get("name"),
            is_active=False
        )
        mail_admins(f"New User created: {new_user}", "", fail_silently=True)

        self.send_activation_email(new_user)
        messages.success(self.request,
                         "You account was created. Please click the confirmation link in the E-Mail to activate it.")
        return new_user


class CustomActivationView(ActivationView):
    success_url = reverse_lazy("login")

    def activate(self, *args, **kwargs):
        username = self.validate_key(kwargs.get("activation_key"))
        user: TenantUser = self.get_user(username)
        user.is_active = True
        user.is_verified = True
        user.save()
        messages.success(self.request, "Account was successfully activated. You can log in now.")

        return user
