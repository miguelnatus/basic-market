from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.urls import resolve
from .models import Tenant, TenantDomain

def _host_plain(request):
    host = request.get_host().split(":", 1)[0].lower()
    return host[4:] if host.startswith("www.") else host

def _split_labels(host):
    return host.split(".")

class DomainTenantMiddleware(MiddlewareMixin):
    def __call__(self, request):
        host = _host_plain(request)
        platform_set = set(getattr(settings, "PLATFORM_DOMAINS", []))
        platform_root = getattr(settings, "PLATFORM_ROOT", None)

        # 1) Custom domain direto?
        td = TenantDomain.objects.select_related("tenant").filter(domain__iexact=host).first()
        if td:
            request.tenant = td.tenant
            return self.get_response(request)

        # 2) Subdomínio do domínio da plataforma (ex.: loja1.basicmarket.com)
        if platform_root and host.endswith("." + platform_root):
            sub = _split_labels(host)[0]
            # tente achar por domain cadastrado (loja1.basicmarket.com) OU por slug
            td2 = TenantDomain.objects.select_related("tenant").filter(domain__iexact=host).first()
            request.tenant = td2.tenant if td2 else Tenant.objects.filter(slug=sub).first()
            if request.tenant:
                return self.get_response(request)

        # 3) Fallback por caminho: /t/<slug>/...
        if host in platform_set:
            match = resolve(request.path_info)
            slug = match.kwargs.get("tenant_slug") if hasattr(match, "kwargs") else None
            if slug:
                request.tenant = Tenant.objects.filter(slug=slug).first()
                return self.get_response(request)
            # Sem slug → plataforma (sem tenant)
            request.tenant = None
            return self.get_response(request)

        # 4) Nada casou → trata como plataforma (ou 404, se preferir)
        request.tenant = None
        return self.get_response(request)