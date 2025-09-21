from django.db import migrations, models

def fill_names(apps, schema_editor):
    Member = apps.get_model("tenants", "Member")
    # blindagem extra: se restar algo nulo ou vazio, preenche
    Member.objects.filter(name__isnull=True).update(name="Membro")
    Member.objects.filter(name="").update(name="Membro")

class Migration(migrations.Migration):

    dependencies = [
        ("tenants", "0004_populate_member_names"),  # sua anterior
    ]

    operations = [
        migrations.RunPython(fill_names, migrations.RunPython.noop),
        migrations.AlterField(
            model_name="member",
            name="name",
            field=models.CharField(max_length=120, null=False, blank=False),
        ),
    ]