# Generated by Django 3.1.4 on 2021-01-10 08:38

from sponsors.models import SponsorTier
from django.db import migrations

TIERS = {
    "diamond": ("Diamond", "corporate"),
    "platinum": ("Platinum", "corporate"),
    "gold": ("Gold", "corporate"),
    "silver": ("Silver", "corporate"),
    "community": ("Community", "non-profit"),
}


def create_sponsor_tiers(apps, schema_editor):
    SponsorTier = apps.get_model("sponsors.SponsorTier")

    for key, (name, type) in TIERS.items():
        SponsorTier.objects.get_or_create(slug=key, name=name, type=type)




class Migration(migrations.Migration):
    dependencies = [
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sponsor_tiers, migrations.RunPython.noop),
    ]
