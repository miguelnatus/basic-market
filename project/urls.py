
from django.contrib import admin
from django.urls import path

from tenants.views import our_team



urlpatterns = [
    path('our-team/', our_team, name='our_team'),
    path('admin/', admin.site.urls),
]
