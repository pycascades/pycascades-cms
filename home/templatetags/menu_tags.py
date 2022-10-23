from django import template
from wagtail.core.models import Page


register = template.Library()


@register.inclusion_tag("tags/navigation.html", takes_context=True)
def render_navigation(context):
    home = Page.objects.get(slug="home")
    return {
        "home": home,
        "menu_pages": home.get_children().filter(live=True, show_in_menus=True),
        "request": context["request"],
    }
