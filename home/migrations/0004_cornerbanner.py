# Generated by Django 3.1.4 on 2021-01-10 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0003_auto_20210110_0738"),
    ]

    operations = [
        migrations.CreateModel(
            name="CornerBanner",
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
                ("text", models.CharField(max_length=255)),
                ("url", models.URLField(blank=True, null=True)),
                ("show_banner", models.BooleanField(default=True)),
            ],
        ),
    ]
