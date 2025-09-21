# tenants/views.py
from django.views.generic import TemplateView
from django.shortcuts import render
from .models import Member
from .utilities import get_tenant

class OurTeamView(TemplateView):
    template_name = "tenants/our_team.html"

    def dispatch(self, request, *args, **kwargs):
        self.tenant = get_tenant(request)  # ou request.tenant se você já tem middleware
        if not self.tenant:
            return render(request, "tenants/no_tenant.html", status=404)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["tenant"] = self.tenant
        ctx["site"] = self.tenant
        ctx["members"] = Member.objects.filter(tenant=self.tenant).order_by("name")
        return ctx