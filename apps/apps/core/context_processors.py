# coding:utf8
from django.conf import settings


def core(request):
    """ """
    return {
        "is_production": settings.IS_PRODUCTION,
        "domain": settings.DOMAIN,
    }
