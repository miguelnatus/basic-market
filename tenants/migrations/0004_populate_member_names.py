from django.db import migrations

def fill_member_names(apps, schema_editor):
    Member = apps.get_model("tenants", "Member")
    # preenche NULL
    Member.objects.filter(name__isnull=True).update(name="Membro")
    # preenche strings vazias (se existirem)
    Member.objects.filter(name__exact="").update(name="Membro")

class Migration(migrations.Migration):

    dependencies = [
        ("tenants", "0003_remove_member_email_remove_member_username_and_more"),
    ]

    operations = [
        migrations.RunPython(fill_member_names, migrations.RunPython.noop),
    ]