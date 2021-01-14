from django.conf import settings
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from wagtail.contrib.modeladmin.helpers import PermissionHelper

from .models import Deployment, NetlifyConfiguration, Log


class DeploymentPermissionHelper(PermissionHelper):
    # remove the add Deployment button
    def user_can_create(self, user):
        return True

    def user_can_edit_obj(self, user, obj):
        return False


class NetlifyConfigurationAdmin(ModelAdmin):
    model = NetlifyConfiguration
    menu_icon = "cogs"
    menu_order = 0
    add_to_settings_menu = True
    inspect_view_enabled = True


class DeploymentAdmin(ModelAdmin):
    model = Deployment
    menu_icon = "success"
    menu_order = 0
    add_to_settings_menu = True

    list_display = (
        "datetime_started",
        "configuration",
        "builder",
        "datetime_finished",
        "deployment_id",
        "url",
    )

    list_filter = ("datetime_started",)

    inspect_view_enabled = True
    permission_helper_class = DeploymentPermissionHelper


class LogsAdmin(ModelAdmin):
    model = Log
    menu_icon = "cogs"
    menu_order = 0
    add_to_settings_menu = True
    inspect_view_enabled = True


if "wagtail.contrib.modeladmin" in settings.INSTALLED_APPS:
    modeladmin_register(NetlifyConfigurationAdmin)
    modeladmin_register(DeploymentAdmin)
    modeladmin_register(LogsAdmin)