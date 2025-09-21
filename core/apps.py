from django.apps import AppConfig

class HomeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "home"         # não mude o label aqui
    # label = "home"      # evite definir label manualmente