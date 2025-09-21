from .base import *
DEBUG = False

# pegue segredos do ambiente:
import os
SECRET_KEY = os.environ["SECRET_KEY"]
ALLOWED_HOSTS = os.environ["ALLOWED_HOSTS"].split(",")  # ex: "annasebba.com.br,www.annasebba.com.br"