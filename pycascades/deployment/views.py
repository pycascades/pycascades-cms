import json

from django.http import HttpResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt

from .models import Deployment
from .redirects import generate_redirect_lines


@csrf_exempt
def success_hook(request):
    """Handle incoming webhook from Netlify, to record deployment completion"""
    body_unicode = request.body.decode("utf-8")
    payload = json.loads(body_unicode)
    # get the first deployment without a Netlify ID
    deploy = Deployment.objects.get(deployment_id=payload["id"])
    deploy.url = payload["url"]
    deploy.message = payload.get("error_message") or ""
    deploy.deployment_url = payload["deploy_ssl_url"]
    deploy.datetime_finished = timezone.now()
    deploy.save()
    return HttpResponse("Thanks\n")


def redirects(request):
    redirects = generate_redirect_lines()
    return HttpResponse("\n".join(redirects))
