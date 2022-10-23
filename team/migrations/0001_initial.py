# Generated by Django 3.1.4 on 2021-01-10 11:48

import django.db.models.deletion
import wagtail.core.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0059_apply_collection_ordering"),
        ("wagtailimages", "0022_uploadedimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="TeamPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("description", wagtail.core.fields.RichTextField()),
            ],
            options={
                "abstract": False,
            },
            bases=("wagtailcore.page",),
        ),
        migrations.CreateModel(
            name="Organizer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("title", models.CharField(blank=True, max_length=255)),
                ("bio", wagtail.core.fields.RichTextField(blank=True)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("twitter", models.CharField(blank=True, max_length=255)),
                (
                    "headshot",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
        ),
    ]
