from .models import Tenant

def get_hostname(request):
    host = request.get_host().split(':')[0]  # Remove port if present
    return host

def get_tenant(request):
    hostname = get_hostname(request)
    try:
        return Tenant.objects.get(domain=hostname)
    except Tenant.DoesNotExist:
        return None