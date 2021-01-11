from django.db import models

from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):

    intro_title = RichTextField(blank=True)
    intro_content = RichTextField(blank=True)

    cover_logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    background = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    custom_template_name = models.CharField(max_length=500, blank=True)

    def get_template(self, request):
        if self.custom_template_name:
            return f"pages/{self.custom_template_name}"
        return "home/home_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("intro_title"),
        FieldPanel("intro_content"),
        MultiFieldPanel([
            ImageChooserPanel("cover_logo"),
            ImageChooserPanel("background"),
        ]),
        FieldPanel("custom_template_name"),
    ]


class SimplePage(Page):
    content = RichTextField(blank=True)

    custom_template_name = models.CharField(max_length=500, blank=True)

    def get_template(self, request):
        if self.custom_template_name:
            return f"pages/{self.custom_template_name}"
        return "pages/simple_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        FieldPanel("custom_template_name"),
    ]


@register_snippet
class CornerBanner(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    show_banner = models.BooleanField(default=True)

    panels = [
        FieldPanel("url"),
        FieldPanel("text"),
        FieldPanel("show_banner"),
    ]

    def __str__(self):
        return self.text
