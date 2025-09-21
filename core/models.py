from django.db import models

class TenantModel(models.Model):
    # Base para todos os modelos de negócio
    tenant = models.ForeignKey("tenancy.Tenant", on_delete=models.CASCADE, db_index=True)

    class Meta:
        abstract = True