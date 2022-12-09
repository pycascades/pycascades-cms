from django import template

from home.models import MastodonVerification


register = template.Library()


@register.inclusion_tag("tags/mastodon.html")
def mastodon_verification():
    return {"accounts": MastodonVerification.objects.all()}


@register.filter
def remove_scheme_prefix(url):
    return url.replace("https://", "").replace("http://", "")
