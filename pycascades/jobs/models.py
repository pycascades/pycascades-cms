from django.db import models
from django.template.defaultfilters import slugify
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page


class JobOverview(Page):
    def get_published_jobs(self):
        return Job.objects.all()


class Job(Page):
    sponsor = models.ForeignKey(
        "sponsors.Sponsor", null=True, on_delete=models.SET_NULL
    )
    description = RichTextField(blank=True)
    location = RichTextField(blank=True)

    post_url = models.CharField(max_length=2000, blank=True)
    apply_url = models.CharField(max_length=2000, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("sponsor"),
        FieldPanel("location"),
        MultiFieldPanel(
            [
                FieldPanel("post_url"),
                FieldPanel("apply_url"),
            ],
            heading="URLs",
        ),
    ]

    def save(self, **kwargs):
        self.slug = slugify(f"{self.sponsor.name}-{self.title}-{self.id}")
        super().save(**kwargs)
