def current_tenant(request):
    return {
        "current_site": getattr(request, "site", None),
        "current_tenant": getattr(request, "tenant", None),
    }