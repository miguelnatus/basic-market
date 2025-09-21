from django.http import Http404
from .utilities import get_tenant

class DomainTenantMiddleware:
    """
    Resolve o Tenant a partir do domínio e injeta em request.tenant.
    Lança 404 se não houver tenant para o domínio acessado.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.tenant = get_tenant(request)
        if request.tenant is None:
            # Você pode trocar por um render para uma página de "domínio não configurado"
            raise Http404("Tenant não encontrado para este domínio.")
        return self.get_response(request)