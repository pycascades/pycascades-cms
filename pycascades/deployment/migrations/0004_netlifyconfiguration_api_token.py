# Generated by Django 3.1.5 on 2021-01-10 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deployment", "0003_deployment_configuration"),
    ]

    operations = [
        migrations.AddField(
            model_name="netlifyconfiguration",
            name="api_token",
            field=models.CharField(default="", max_length=200),
        ),
    ]
