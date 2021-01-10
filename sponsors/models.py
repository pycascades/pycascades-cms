from django.db import models

from wagtail.core.models import Page
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=255)

    website = models.URLField(blank=True)
    description = RichTextField(blank=True)

    tier = models.ForeignKey(
        'sponsors.SponsorTier',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='sponsors'
    )

    logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    logo_dark_background = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    sign_date = models.DateField()

    panels = [
        FieldPanel('name'),
        SnippetChooserPanel('tier'),
        FieldPanel("website"),
        FieldPanel("description"),
        FieldPanel("sign_date"),
        MultiFieldPanel([
            ImageChooserPanel('logo'),
            ImageChooserPanel('logo_dark_background'),
        ]),
    ]

    def __str__(self):
        return self.name


@register_snippet
class SponsorTier(models.Model):
    prepopulated_fields = {"slug": ("name",)}


    CORPORATE = "corporate"
    NPO = "non-profit"

    TYPE_CHOICES = (
        (CORPORATE, "Corporate"),
        (NPO, "Non-Profit / Academic / Startup")
    )

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)

    panels = [
        FieldPanel('name'),
        FieldPanel('type'),
    ]

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"