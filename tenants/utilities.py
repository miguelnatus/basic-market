from typing import Optional
from django.http import HttpRequest
from .models import Tenant

def get_host_domain(request: HttpRequest) -> str:
    """
    Extrai o host da requisição, sem porta, normalizado em minúsculas
    e sem o prefixo 'www.' (para aceitar tanto empresa.com quanto www.empresa.com).
    """
    host = request.get_host().split(':', 1)[0].lower()
    if host.startswith('www.'):
        host = host[4:]
    return host

def get_tenant(request: HttpRequest) -> Optional[Tenant]:
    """
    Retorna o Tenant correspondente ao domínio acessado (ou None se não houver).
    """
    domain = get_host_domain(request)
    return Tenant.objects.filter(domain__iexact=domain).first()