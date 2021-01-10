import os
import django_heroku

from pycascades.settings.dev import SECRET_KEY
from .base import *

DEBUG = False

SECRET_KEY = os.getenv("SECRET_KEY", "")
ALLOWED_HOSTS = ["pycascades-cms.herokuapp.com"]


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = "pycascades-cms-files"
AWS_S3_ENDPOINT_URL = "https://sfo2.digitaloceanspaces.com"

django_heroku.settings(locals())