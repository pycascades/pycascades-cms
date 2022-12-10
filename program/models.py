import json

from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.core.fields import RichTextField
from wagtail.core.models import Orderable, Page
from wagtail.snippets.models import register_snippet


class PretalxSchedule(Page):
    pretalx_event_url = models.URLField(verbose_name="Pretalx Event URL", blank=True)
    widget_head_code = models.CharField(max_length=2000)
    widget_embed_code = models.TextField()

    def get_template(self, request, *args, **kwargs):
        return "program/pretalx_schedule.html"

    content_panels = Page.content_panels + [
        FieldPanel("pretalx_event_url"),
        FieldPanel("widget_head_code"),
        FieldPanel("widget_embed_code"),
    ]

    def get_context(self, request):
        context = super().get_context(request)

        context["talk_map"] = self.get_talk_pretalx_map()
        return context

    def get_talk_pretalx_map(self):
        talk_map = {}
        talks = Talk.objects.all()
        for talk in talks:
            talk_map[talk.external_id] = talk.url
        return json.dumps(talk_map)


class TalkList(Page):
    def get_published_speakers(self):
        return Speaker.objects.live().order_by("talk__title")

    def get_published_talks(self):
        return Talk.objects.live().order_by("start_time", "title")


@register_snippet
class Talk(Page):
    abstract = RichTextField(blank=True)

    slides = models.URLField(blank=True, null=True)
    video = models.URLField(blank=True, null=True)

    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)

    external_id = models.CharField(blank=True, max_length=255)

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
        FieldPanel("external_id"),
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
    mastodon = models.CharField(max_length=200, blank=True)
    instagram = models.CharField(max_length=200, blank=True)
    github = models.CharField(max_length=200, blank=True)
    website = models.URLField(blank=True)

    bio = RichTextField(blank=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("bio"),
        FieldPanel("headshot"),
        MultiFieldPanel(
            [
                FieldPanel("twitter_handle", heading="Twitter (username only)"),
                FieldPanel("instagram", heading="Instagram (username only)"),
                FieldPanel("github", heading="GitHub (username only)"),
                FieldPanel("mastodon", heading="Mastodon (full URL)"),
                FieldPanel("website"),
            ]
        ),
    ]

    def __str__(self):
        return f"{self.name}"
