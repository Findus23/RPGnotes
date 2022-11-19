from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext_lazy as _

from tenant_users.tenants.models import UserProfile


class TenantUser(UserProfile):
    name = models.CharField(
        _("Name"),
        max_length=100,
        # blank=True,
    )

    email = models.EmailField(
        _('Email Address'),
        unique=True,
        db_index=True,
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def get_short_name(self):
        return self.name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    @property
    def username(self):
        return self.name

    @property
    def graphkey(self):
        return f"use{self.pk}"
