from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest

from campaigns.models import Campaign
from users.models import TenantUser


class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request: HttpRequest):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        current_user: TenantUser = request.user
        tenant: Campaign = request.tenant
        if tenant.pk == 1 \
                or request.path.startswith("/login") \
                or request.path.startswith("/css"):
            return self.get_response(request)
        if not current_user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not current_user.tenants.filter(pk=tenant.pk).exists():
            raise PermissionDenied()
        return self.get_response(request)
