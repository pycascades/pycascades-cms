from django.db import models
from django.template.defaultfilters import slugify


from modelcluster.models import ClusterableModel

from wagtail.core.models import Page, Orderable
from wagtail.images.models import Image
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel


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