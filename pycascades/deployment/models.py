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
    configuration = models.ForeignKey(
        NetlifyConfiguration,
        related_name="deploys",
        null=True,
        on_delete=models.SET_NULL,
    )

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
    if instance.deployment_id:
        return

    # this uses the Wagtail Bakery command to generate
    # static pages in the specified subdirectory
    call_command("build")

    config = instance.configuration
    api_request = pynetlify.APIRequest(config.api_token)
    netlify_site = api_request.get_site(config.netlify_id)

    instance.deployment_id = api_request.deploy_folder_to_site(
        settings.BUILD_DIR, netlify_site
    )
    instance.save()

    connection.close()


signals.post_save.connect(deploy, sender=Deployment)
