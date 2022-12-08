from django.conf import settings


EXPOSED_SETTINGS = [
    "IS_LIVE",
    "SITE_URL",
    "SECURE_SITE_URL",
    "CONTACT_EMAIL",
    "CONDUCT_EMAIL",
    "META_DESCRIPTION",
    "GOOGLE_ANALYTICS_ID",
    "TWITTER_URL",
    "INSTAGRAM_URL",
    "INSTAGRAM_USER_ID",
    "INSTAGRAM_USERNAME",
    "INSTAGRAM_ACCESS_TOKEN",
    "VOLUNTEER_URL",
    "CFP_URL",
    "SPONSORSHIP_PROSPECTUS_URL",
    "SLACK_URL",
    "MASTODON_URL",
    "CONFERENCE_YEAR",
]


def exposed_settings(request):

    context = {}
    for key in EXPOSED_SETTINGS:
        context[key] = getattr(settings, key, "")

    return context
