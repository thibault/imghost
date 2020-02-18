import os
from sys import path
from os.path import basename
from unipath import Path
from logging.handlers import SysLogHandler


DJANGO_ROOT = Path(__file__).ancestor(3)
PROJECT_ROOT = DJANGO_ROOT.ancestor(1)
SITE_NAME = basename(PROJECT_ROOT)
CONFIGURATION_APP_ROOT = Path(__file__).ancestor(2)
PUBLIC_ROOT = PROJECT_ROOT.child('public')
path.append(DJANGO_ROOT)
path.append(CONFIGURATION_APP_ROOT)

SECRET_KEY = '7dcckq$8m2)mzwgu6&u#7+g4(3u#dl4k%9m9afpw+p-4!!!+ar'

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'pipeline',
    'widget_tweaks',
)

LOCAL_APPS = (
    'images',
    'memes',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'core.urls'

WSGI_APPLICATION = 'core.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = PUBLIC_ROOT.child('static')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    DJANGO_ROOT.child('static'),
)

MEDIA_ROOT = PUBLIC_ROOT.child('media')
MEDIA_URL = '/media/'


FORM_RENDERER = 'django.forms.renderers.TemplatesSetting'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [DJANGO_ROOT.child('templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'debug': False,
            'context_processors': [
                'django.template.context_processors.i18n',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.core.context_processors.request',
            ],
        },
    },
]

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE = {
    # 'JS_COMPRESSOR': None
    'STYLESHEETS': {
        'base': {
            'source_filenames': (
                'css/bootstrap.css',
                'css/project.css',
            ),
            'output_filename': 'css/base.css',
        },
    },
    'JAVASCRIPT': {
        'base': {
            'source_filenames': (
                'js/jquery.js',
                'js/bootstrap.js',
            ),
            'output_filename': 'js/base.js',
        },
        'meme': {
            'source_filenames': (
                'js/meme.js',
            ),
            'output_filename': 'js/meme.js',
        },
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'verbose': {
            'format': '[phase] %(levelname)s %(asctime)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
        # Send info messages to syslog
        'syslog': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'facility': SysLogHandler.LOG_LOCAL2,
            'address': '/dev/log',
            'formatter': 'verbose',
        },
        'mail_admins': {
            'level': 'WARNING',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
        },
        # critical errors are logged to sentry
        #'sentry': {
        #    'level': 'ERROR',
        #    'filters': ['require_debug_false'],
        #    'class': 'raven.contrib.django.handlers.SentryHandler',
        #},
    },
    'loggers': {
        # This is the "catch all" logger
        '': {
            'handlers': ['console', 'syslog', 'mail_admins'],
            'level': 'DEBUG',
            'propagate': False,
        },
        # We have to redefine this. See
        # http://stackoverflow.com/questions/20282521/django-request-logger-not-propagated-to-root
        'django.request': {
            'propagate': True,
        },
    }
}
