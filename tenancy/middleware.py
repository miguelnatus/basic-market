from django.utils.deprecation import MiddlewareMixin
from wagtail.models import Site

class CurrentTenantMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Resolve o site do Wagtail pelo host/porta da requisição
        site = Site.find_for_request(request)
        request.site = site
        request.tenant = getattr(site, "tenant", None)