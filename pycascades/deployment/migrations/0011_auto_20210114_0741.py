# Generated by Django 3.1.5 on 2021-01-14 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deployment", "0010_auto_20210114_0737"),
    ]

    operations = [
        migrations.AlterField(
            model_name="log",
            name="deploy",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="logs",
                to="deployment.deployment",
            ),
        ),
    ]
