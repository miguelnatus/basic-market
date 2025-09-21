# tenants/mixins.py
from django.shortcuts import render
from .utilities import get_tenant

class TenantMixin:
    def dispatch(self, request, *args, **kwargs):
        self.tenant = getattr(request, "tenant", None) or get_tenant(request)
        if not self.tenant:
            return render(request, "tenants/no_tenant.html", status=404)
        return super().dispatch(request, *args, **kwargs)