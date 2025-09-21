from django.db import models

class Tenant(models.Model):
    name = models.CharField(max_length=100)
    domain = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.domain})"

class Member(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.PROTECT, related_name="members")
    name = models.CharField(max_length=120)
    role = models.CharField(max_length=120, blank=True)
    photo = models.ImageField(upload_to="members/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} – {self.tenant.name}"