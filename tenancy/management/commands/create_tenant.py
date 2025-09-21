from django.core.management.base import BaseCommand, CommandError
from django.utils.text import slugify
from wagtail.models import Page, Site
from tenancy.models import Tenant
from home.models import HomePage

class Command(BaseCommand):
    help = "Cria um Tenant + Site no Wagtail (domínio, raiz e homepage)."

    def add_arguments(self, parser):
        parser.add_argument("--name", required=True, help="Nome do cliente")
        parser.add_argument("--domain", required=True, help="Hostname (ex.: cliente.local)")
        parser.add_argument("--port", type=int, default=80, help="Porta (dev: 8000, prod: 80/443)")
        parser.add_argument("--site_name", help="Nome a exibir no admin Wagtail (opcional)")

    def handle(self, *args, **opts):
        name = opts["name"].strip()
        domain = opts["domain"].strip().lower()
        port = opts["port"]
        site_name = opts.get("site_name") or name

        if Site.objects.filter(hostname=domain, port=port).exists():
            raise CommandError("Já existe um Site com esse domínio/porta.")

        root_page = Page.get_first_root_node()
        homepage_title = f"Home – {name}"

        homepage = HomePage(title=homepage_title)
        root_page.add_child(instance=homepage)
        homepage.save_revision().publish()

        site = Site.objects.create(
            hostname=domain,
            port=port,
            site_name=site_name,
            root_page=homepage,
            is_default_site=False,
        )

        tenant = Tenant.objects.create(
            site=site,
            name=name,
            slug=slugify(name)[:50],
            is_active=True,
        )

        self.stdout.write(self.style.SUCCESS(
            f"Tenant criado: {tenant} | HomePage id={homepage.id} | Site id={site.id}"
        ))
