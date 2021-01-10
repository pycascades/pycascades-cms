from django.conf.urls import url
from .views import success_hook, redirects

urlpatterns = [
    url(r"^success$", success_hook, name="success_hook"),
    url(r"^redirects$", redirects, name="redirect_builder"),
]
