from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel


class NewsList(Page):
    @property
    def hide_children(self):
        return True


class NewsPost(Page):
    content = RichTextField()
    teaser = RichTextField(blank=True)

    date = models.DateField()

    content_panels = Page.content_panels + [
        FieldPanel("content"),
        FieldPanel("teaser"),
        FieldPanel("date"),
    ]
