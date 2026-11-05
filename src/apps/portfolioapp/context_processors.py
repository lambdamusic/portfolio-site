from django.conf import settings


def site_url(request):
    """Expose SITE_URL to templates, e.g. for the canonical link."""
    return {'SITE_URL': settings.SITE_URL}
