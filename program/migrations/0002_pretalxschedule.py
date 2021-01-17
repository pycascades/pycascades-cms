# Generated by Django 3.1.5 on 2021-01-17 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PretalxSchedule',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('pretalx_event_url', models.URLField(verbose_name='Pretalx Event URL')),
                ('widget_head_code', models.CharField(max_length=2000)),
                ('widget_embed_code', models.TextField()),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
