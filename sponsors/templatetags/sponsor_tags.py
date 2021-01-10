from django import template
from sponsors.models import Sponsor, SponsorTier

register = template.Library()


@register.simple_tag
def corporate_sponsors():
    return Sponsor.objects.filter(tie__slug=SponsorTier.CORPORATE)


@register.simple_tag
def non_profit_sponsors():
    return Sponsor.objects.filter(tie__slug=SponsorTier.NPO)


@register.simple_tag
def corporate_tiers():
    return SponsorTier.objects.filter(
        sponsors__isnull=False, type=SponsorTier.CORPORATE
    )


@register.simple_tag
def npo_tiers():
    return SponsorTier.objects.filter(sponsors__isnull=False, type=SponsorTier.NPO)
