# Generated by Django 3.1.5 on 2021-01-14 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0022_uploadedimage"),
        ("sponsors", "0003_auto_20210110_1012"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sponsor",
            name="logo_dark_background",
            field=models.ForeignKey(
                blank=True,
                help_text="Logo displayed in the footer (max height 70px)",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
