from django import template
from home.models import CornerBanner

register = template.Library()


@register.inclusion_tag("tags/corner_banner.html", takes_context=True)
def corner_banner(context):
    return {
        "banner": CornerBanner.objects.all().first(),
        "request": context["request"],
    }
