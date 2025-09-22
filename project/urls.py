from django.contrib import admin
from django.urls import path
from tenants.views import HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),            # plataforma OU tenant (via host)
    path("t/<slug:tenant_slug>/", HomeView.as_view()),    # fallback por caminho (opcional)
    path("admin/", admin.site.urls),
]