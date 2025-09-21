from django.http import Http404

class TenantQuerysetMixin:
    """Para CBVs: filtra automaticamente por request.tenant"""
    def get_queryset(self):
        qs = super().get_queryset()
        tenant = getattr(self.request, "tenant", None)
        if not tenant:
            raise Http404("Tenant não encontrado")
        return qs.filter(tenant=tenant)