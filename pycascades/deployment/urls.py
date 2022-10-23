from django.conf.urls import url

from .views import redirects, success_hook


urlpatterns = [
    url(r"^success$", success_hook, name="success_hook"),
    url(r"^redirects$", redirects, name="redirect_builder"),
]
