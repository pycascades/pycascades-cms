from django.urls import re_path

from .views import redirects, success_hook


urlpatterns = [
    re_path(r"^success$", success_hook, name="success_hook"),
    re_path(r"^redirects$", redirects, name="redirect_builder"),
]
