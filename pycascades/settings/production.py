import os

import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .base import *  # noqa: F401, F403


sentry_sdk.init(
    dsn=os.getenv("SENTRY_DSN"),
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,
    send_default_pii=True,
)

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY", "")
ALLOWED_HOSTS = ["pycascades-cms.herokuapp.com"]

if os.getenv("RUN_LOCAL_STATIC_GEN"):
    print("RUNNING STATIC GEN")
    MEDIA_ROOT = "_build/media/"
else:
    print("RUNNING NORMAL")
    DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "pycascades-cms-files"
AWS_S3_ENDPOINT_URL = "https://sfo2.digitaloceanspaces.com"

# HTTP to HTTPS redirect
# https://github.com/pycascades/pycascades-cms/issues/46
SECURE_SSL_REDIRECT = True

django_heroku.settings(locals())
