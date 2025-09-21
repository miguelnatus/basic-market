from .base import *
DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "annasebba.local"]
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


# try:
#     from .local import *
# except ImportError:
#     pass
