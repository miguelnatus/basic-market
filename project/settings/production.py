from .base import *
from dotenv import load_dotenv

load_dotenv()
DEBUG = False

# pegue segredos do ambiente:
import os
SECRET_KEY = os.getenv("SECRET_KEY")
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS").split(",")  # ex: "annasebba.com.br,www.annasebba.com.br"