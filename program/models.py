from django.db import models
from django.db.models.fields import Field

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.images.models import Image
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet


class TalkList(Page):
    def get_published_speakers(self):
        return Speaker.objects.all().order_by("talk__title")

    def get_published_talks(self):
        return Talk.objects.all().order_by("start_time", "title")


@register_snippet
class Talk(Page):
    abstract = RichTextField(blank=True)

    slides = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)

    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    content_panels = [
        FieldPanel("title"),
        FieldPanel("abstract"),
        InlinePanel("speakers", label="Speakers"),
        MultiFieldPanel(
            [
                FieldPanel("slides"),
                FieldPanel("video"),
            ],
            heading="Talk Links",
        ),
        MultiFieldPanel(
            [
                FieldPanel("start_time"),
                FieldPanel("end_time"),
            ],
            heading="Time Slot",
        ),
    ]

    def __str__(self):
        return f"{self.title}"


class Speaker(Orderable):
    name = models.CharField(max_length=200)
    talk = ParentalKey("Talk", related_name="speakers")

    headshot = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    company = models.CharField(max_length=200, blank=True)

    twitter_handle = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)

    bio = RichTextField(blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("bio"),
        ImageChooserPanel("headshot"),
        MultiFieldPanel(
            [
                FieldPanel("twitter_handle"),
                FieldPanel("website"),
            ]
        ),
    ]

    def __str__(self):
        return f"{self.name}"
