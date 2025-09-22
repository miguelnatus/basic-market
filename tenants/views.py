from django.views.generic import TemplateView
from django.template.loader import select_template
from django.http import HttpResponse

def _clean_domain(h: str) -> str:
    h = h.split(":", 1)[0].lower()
    return h[4:] if h.startswith("www.") else h

class HomeView(TemplateView):
    system_template = "system/home.html"      # plataforma
    tenant_fallback = "tenants/home.html"     # fallback

    def get(self, request, *args, **kwargs):
        tenant = getattr(request, "tenant", None)
        if tenant:
            domain = _clean_domain(request.get_host())
            tpl = select_template([f"sites/{domain}/home.html", self.tenant_fallback])
            ctx = {"tenant": tenant}
            return HttpResponse(tpl.render(ctx, request))
        tpl = select_template([self.system_template])
        return HttpResponse(tpl.render({"product_name": "Basic Market"}, request))