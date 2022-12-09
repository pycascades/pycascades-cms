from django import template

from home.models import MastodonVerification


register = template.Library()


@register.inclusion_tag("tags/mastodon.html")
def mastodon_verification():
    return {"accounts": MastodonVerification.objects.all()}
