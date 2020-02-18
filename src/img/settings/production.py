from .base import *  # noqa
from django.core.exceptions import ImproperlyConfigured

try:
    import prod_private
except ImportError:
    raise ImproperlyConfigured("Create a prod_private.py file in settings")


def get_prod_setting(setting):
    """Get the setting or return exception """
    try:
        return getattr(prod_private, setting)
    except AttributeError:
        error_msg = "The %s setting is missing from prod settings" % setting
        raise ImproperlyConfigured(error_msg)


INSTALLED_APPS += (
    'gunicorn',
)

DATABASES = get_prod_setting('DATABASES')

SECRET_KEY = get_prod_setting('SECRET_KEY')

ALLOWED_HOSTS = get_prod_setting('ALLOWED_HOSTS')
