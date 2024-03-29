from django.core.exceptions import PermissionDenied
from django.http import HttpRequest, HttpResponse

from campaigns.models import Campaign
from pdf.utils import create_document


def pdf(request: HttpRequest) -> HttpResponse:
    if not request.user.is_known:
        raise PermissionDenied
    tenant: Campaign = request.tenant
    create_document(tenant)

    response = HttpResponse(tenant.document.file, content_type='application/pdf')
    response['Content-Disposition'] = f'inline; filename={"document.pdf"}'
    return response
