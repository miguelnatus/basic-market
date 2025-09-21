# project/urls.py
from django.contrib import admin
from django.urls import path
from tenants.views import OurTeamView

urlpatterns = [
    path("our-team/", OurTeamView.as_view(), name="our_team"),
    path("admin/", admin.site.urls),
]
