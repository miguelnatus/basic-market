from django.db import migrations
from django.utils.text import slugify

def gen_unique_slug(base, taken):
    """
    Gera slug único: "base", "base-2", "base-3", ...
    """
    base = base[:55].strip("-") or "site"
    slug = base
    i = 2
    while slug in taken:
        # reserva alguns caracteres para o sufixo
        slug = f"{base[:55]}-{i}"
        i += 1
    taken.add(slug)
    return slug

def fill_slugs(apps, schema_editor):
    Tenant = apps.get_model("tenants", "Tenant")
    taken = set(
        Tenant.objects.exclude(slug__isnull=True).exclude(slug__exact="").values_list("slug", flat=True)
    )

    for t in Tenant.objects.all().order_by("id"):
        if t.slug:
            # já tem slug, só garante que não conflita
            if t.slug in taken:
                base = slugify(t.name or t.domain or "site")
                t.slug = gen_unique_slug(base, taken)
                t.save(update_fields=["slug"])
            else:
                taken.add(t.slug)
            continue

        base = slugify(t.name or t.domain or "site")
        t.slug = gen_unique_slug(base, taken)
        t.save(update_fields=["slug"])

class Migration(migrations.Migration):

    dependencies = [
        # substitua pelo nome da migração anterior que adicionou o campo slug
        ("tenants", "0006_tenant_slug_alter_tenant_domain_alter_tenant_name_and_more"),
    ]

    operations = [
        migrations.RunPython(fill_slugs, migrations.RunPython.noop),
    ]