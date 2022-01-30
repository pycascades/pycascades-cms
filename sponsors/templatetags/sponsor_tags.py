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
    ).distinct()


@register.simple_tag
def npo_tiers():
    return SponsorTier.objects.filter(
        sponsors__isnull=False, type=SponsorTier.NPO
    ).distinct()


@register.inclusion_tag("sponsors/sponsor_logos_smol.html")
def sponsor_footer():
    return {"sponsors": Sponsor.objects.filter(tier__type=SponsorTier.CORPORATE)}
