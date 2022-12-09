from django.db import models
from django.db.models.fields import EmailField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Page
from wagtail.snippets.models import register_snippet


class TeamPage(Page):
    description = RichTextField()

    content_panels = Page.content_panels + [FieldPanel("description")]


@register_snippet
class Organizer(models.Model):
    CHAIR_SECTION = "chair"
    ORGANIZER_SECTION = "organizer"
    EMERITUS_SECTION = "emeritus"

    SECTIONS = (
        (CHAIR_SECTION, CHAIR_SECTION),
        (ORGANIZER_SECTION, ORGANIZER_SECTION),
        (EMERITUS_SECTION, EMERITUS_SECTION),
    )

    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255, blank=True)
    bio = RichTextField(blank=True)
    section = models.CharField(
        max_length=50, choices=SECTIONS, default=ORGANIZER_SECTION
    )

    email = EmailField(blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    mastodon = models.CharField(max_length=255, blank=True)

    headshot = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("title"),
        FieldPanel("section"),
        FieldPanel("bio"),
        MultiFieldPanel(
            [
                FieldPanel("email"),
                FieldPanel("twitter", heading="Twitter (username only)"),
                FieldPanel("mastodon", heading="Mastodon (full URL)"),
            ]
        ),
        FieldPanel("headshot"),
    ]

    def __str__(self):
        return f"{self.name} ({self.title})"
