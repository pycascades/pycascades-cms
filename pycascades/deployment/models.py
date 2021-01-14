import os
import subprocess

from threading import Thread
from django.db import models
from django.core.management import call_command
from django.db import connection
from django.conf import settings
from django.utils.module_loading import import_string
from django.db.models import signals

from pynetlify import pynetlify

from wagtail.core.signals import page_published
from wagtail.admin.edit_handlers import FieldPanel


class NetlifyConfiguration(models.Model):
    name = models.CharField(max_length=30)
    netlify_id = models.CharField(max_length=100)
    api_token = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.name


class Deployment(models.Model):
    BAKERY_BUILD = "build"
    NETLIFY_BUILD = "netlify_build"

    BUILD_CHOICES = (
        (BAKERY_BUILD, "Default Wagtail Build"),
        (NETLIFY_BUILD, "Custom PyCascades Build"),
    )

    configuration = models.ForeignKey(
        NetlifyConfiguration,
        related_name="deploys",
        null=True,
        on_delete=models.SET_NULL,
    )
    builder = models.CharField(
        max_length=100, choices=BUILD_CHOICES, default=NETLIFY_BUILD
    )

    logs = models.TextField()

    deployment_id = models.CharField(max_length=200, blank=True)
    message = models.CharField(max_length=200, blank=True)

    url = models.URLField(null=True)
    deployment_url = models.URLField(null=True)
    datetime_started = models.DateTimeField(
        auto_now_add=True, help_text="deployment started"
    )
    datetime_finished = models.DateTimeField("deployment completed", null=True)

    panels = [
        FieldPanel("configuration"),
        FieldPanel("builder"),
    ]

    def __str__(self):
        return f"Deploy to {self.configuration.name}"


def postpone(function):
    """
    Cheap aysnc, see https://stackoverflow.com/a/28913218
    """

    def decorator(*args, **kwargs):
        t = Thread(target=function, args=args, kwargs=kwargs)
        t.daemon = True
        t.start()

    return decorator


@postpone
def deploy(sender, instance, **kwargs):
    """
    Trigger a build on Netlify, if NETLIFY_BUILD_HOOK is supplied, or
    build static pages, then upload incremental changes to Netlify.
    """
    if instance.deployment_id or instance.logs:
        return

    instance.logs = "Started..."
    instance.save()

    # this uses the Wagtail Bakery command to generate
    # static pages in the specified subdirectory

    print("getting all remote files")
    remote_build = subprocess.check_output(["python", "manage.py", instance.builder])

    instance.logs = remote_build
    instance.save()

    env = os.environ.copy()
    env["RUN_LOCAL_STATIC_GEN"] = "1"

    print("running local build")
    local_build = subprocess.check_output(
        ["python", "manage.py", instance.builder, "--keep-build-dir", "--skip-media"],
        env=env,
    )

    instance.logs += local_build
    instance.save()

    config = instance.configuration
    api_request = pynetlify.APIRequest(config.api_token)
    netlify_site = api_request.get_site(config.netlify_id)

    instance.logs += f"\n\nDeploying {settings.BUILD_DIR}"

    instance.deployment_id = api_request.deploy_folder_to_site(
        settings.BUILD_DIR, netlify_site
    )
    instance.save()

    connection.close()


signals.post_save.connect(deploy, sender=Deployment)
