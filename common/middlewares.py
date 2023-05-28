from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied
from django.http import HttpRequest
from django.template.response import TemplateResponse

from campaigns.models import Campaign
from rpg_notes.settings import DEBUG
from users.models import TenantUser

demo_campaign_id = 4 if DEBUG else 8


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
        if tenant.pk == demo_campaign_id:
            if request.method in {"GET", "HEAD"} or request.path.startswith("/i18n/setlang"):
                return self.get_response(request)
            elif not current_user.is_authenticated:
                r = TemplateResponse(request, "common/demo_readonly.jinja", status=405)
                r.render()
                return r
        if not current_user.is_authenticated:
            return redirect_to_login(request.get_full_path())
        if not current_user.tenants.filter(pk=tenant.pk).exists():
            raise PermissionDenied()
        return self.get_response(request)
