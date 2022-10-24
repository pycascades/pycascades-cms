# Generated by Django 3.2.16 on 2022-10-23 04:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0011_auto_20210114_0741'),
    ]

    operations = [
        migrations.AddField(
            model_name='netlifyconfiguration',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='deployment',
            name='configuration',
            field=models.ForeignKey(limit_choices_to={'active': True}, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='deploys', to='deployment.netlifyconfiguration'),
        ),
    ]
