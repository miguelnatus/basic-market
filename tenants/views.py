from django.shortcuts import render

from .models import Tenant, Member
from .utilities import get_tenant

def our_team(request):
    tenant = get_tenant(request)
    site = Tenant.objects.filter(domain=get_tenant(request))
    if not tenant:
        return render(request, 'tenants/no_tenant.html')

    members = Member.objects.filter(tenant=tenant)
    print(site)
    return render(request, 'tenants/our_team.html', {'site': site, 'tenant': tenant, 'members': members})