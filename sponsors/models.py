from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.snippets.models import register_snippet


@register_snippet
class Sponsor(models.Model):
    name = models.CharField(max_length=255)

    website = models.URLField(blank=True)
    description = RichTextField(blank=True)

    tier = models.ForeignKey(
        "sponsors.SponsorTier",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="sponsors",
    )

    logo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    logo_dark_background = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
        help_text="Logo displayed in the footer (max height 70px)",
    )

    sign_date = models.DateField()

    panels = [
        FieldPanel("name"),
        FieldPanel("tier"),
        FieldPanel("website"),
        FieldPanel("description"),
        FieldPanel("sign_date"),
        MultiFieldPanel(
            [
                FieldPanel("logo"),
                FieldPanel("logo_dark_background"),
            ]
        ),
    ]

    def __str__(self):
        return self.name


@register_snippet
class SponsorTier(models.Model):
    prepopulated_fields = {"slug": ("name",)}

    CORPORATE = "corporate"
    NPO = "non-profit"

    TYPE_CHOICES = ((CORPORATE, "Corporate"), (NPO, "Non-Profit / Academic / Startup"))

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True)
    type = models.CharField(max_length=255, choices=TYPE_CHOICES)
    priority = models.PositiveSmallIntegerField(
        default=0,
        help_text="Sorting order on the page (higher number means higher up)",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
        FieldPanel("type"),
        FieldPanel("priority"),
    ]

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
