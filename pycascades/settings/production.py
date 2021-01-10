import os
import django_heroku

from pycascades.settings.dev import SECRET_KEY
from .base import *

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY", "")
ALLOWED_HOSTS = ["pycascades-cms.herokuapp.com"]

django_heroku.settings(locals())