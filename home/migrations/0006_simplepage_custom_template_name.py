# Generated by Django 3.1.5 on 2021-01-11 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_simplepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="simplepage",
            name="custom_template_name",
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
