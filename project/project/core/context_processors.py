from django.conf import settings

from .models import SiteCustomization


def check_debug(request):
    return {'DEBUG': settings.DEBUG}


def site_customization(request):
    """Manage website description data.
    Args:
        request:
    Returns:
        JSON
    """
    data = SiteCustomization.objects.filter(id=1)
    protocol = request.scheme

    response = {
        'data': data,
        'protocol': protocol,
    }

    return response
