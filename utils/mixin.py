from django.contrib.auth.mixins import AccessMixin

from users.models import TenantUser


class PartOfTenantRequiredMixin(AccessMixin):
    """Verify that the current user is authenticated."""

    permission_denied_message = "You are not part of this campaign"

    def dispatch(self, request, *args, **kwargs):
        current_user: TenantUser = self.request.user

        if not current_user.tenants.filter(pk=self.request.tenant.pk).exists():
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
