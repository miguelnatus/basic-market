from django.db import models
from django.utils.text import slugify
from wagtail.models import Site

class Tenant(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name="tenant")
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)[:50]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.site.hostname})"