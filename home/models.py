from django.db import models

from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


class HomePage(Page):
    cover_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    intro_title = RichTextField(blank=True)
    intro_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        ImageChooserPanel('cover_logo'),
        FieldPanel('intro_title'),
        FieldPanel('intro_content'),
    ]


@register_snippet
class CornerBanner(models.Model):
    text = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    show_banner = models.BooleanField(default=True)

    panels = [
        FieldPanel('url'),
        FieldPanel('text'),
        FieldPanel('show_banner'),
    ]

    def __str__(self):
        return self.text