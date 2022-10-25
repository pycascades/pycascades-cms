from django import template

from team.models import Organizer


register = template.Library()


@register.simple_tag
def organizers(section):
    return Organizer.objects.filter(section=section).order_by("name")
