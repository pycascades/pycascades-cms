# Generated by Django 4.1.3 on 2022-12-09 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("program", "0004_add_mastodon_to_speakers_organizers"),
    ]

    operations = [
        migrations.AddField(
            model_name="speaker",
            name="github",
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name="speaker",
            name="instagram",
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
