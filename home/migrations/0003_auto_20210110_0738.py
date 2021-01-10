# Generated by Django 3.1.4 on 2021-01-10 07:38

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0022_uploadedimage"),
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="cover_logo",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
        migrations.AddField(
            model_name="homepage",
            name="intro_content",
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="intro_title",
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
    ]
