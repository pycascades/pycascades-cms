from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
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
    background_attribution = models.TextField(
        blank=True, verbose_name="Background image attribution"
    )

    custom_template_name = models.CharField(max_length=500, blank=True)

    def get_template(self, request):
        if self.custom_template_name:
            return [self.custom_template_name, f"pages/{self.custom_template_name}"]
        return "home/home_page.html"

    content_panels = Page.content_panels + [
        FieldPanel("intro_title"),
        FieldPanel("intro_content"),
        MultiFieldPanel(
            [
                FieldPanel("cover_logo"),
                FieldPanel("background"),
                FieldPanel("background_attribution"),
            ]
        ),
        FieldPanel("custom_template_name"),
    ]


class VenuePage(Page):

    venue_content = RichTextField(blank=True)
    venue_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    venue_attribution = models.TextField(
        blank=True,
        verbose_name="Venue image attribution",
        help_text="HTML allowed",
    )

    location_address = RichTextField()
    location_lat = models.DecimalField(max_digits=20, decimal_places=17)
    location_long = models.DecimalField(max_digits=20, decimal_places=17)
    location_google_maps_url = models.CharField(max_length=500, blank=True)

    accommodation_content = RichTextField(blank=True)
    accommodation_photo = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    accommodation_attribution = models.TextField(
        blank=True,
        verbose_name="Accommodation image attribution",
        help_text="HTML allowed",
    )

    def get_template(self, *args, **kwargs):
        return "home/venue_page.html"

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("venue_content"),
                FieldPanel("venue_photo"),
                FieldPanel("venue_attribution"),
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel("location_address"),
                FieldPanel("location_lat"),
                FieldPanel("location_long"),
                FieldPanel("location_google_maps_url"),
            ]
        ),
        MultiFieldPanel(
            [
                FieldPanel("accommodation_content"),
                FieldPanel("accommodation_photo"),
                FieldPanel("accommodation_attribution"),
            ]
        ),
    ]


class SimplePage(Page):
    content = RichTextField(blank=True)

    custom_template_name = models.CharField(max_length=500, blank=True)

    def get_template(self, request):
        if self.custom_template_name:
            return [self.custom_template_name, f"pages/{self.custom_template_name}"]
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


@register_snippet
class MastodonVerification(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(
        max_length=255,
        help_text="e.g. fosstodon.org/@pycascades",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("url"),
    ]

    def __str__(self):
        return f"{self.name} ({self.url})"
