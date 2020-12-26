import os
import dj_database_url

from pycascades.settings.dev import SECRET_KEY
from .base import *

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY", "")
ALLOWED_HOSTS = ["pycascades-cms.herokuapp.com"]

DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


try:
    from .local import *
except ImportError:
    pass
