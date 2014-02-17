import os
from sys import path
from os.path import basename
from unipath import Path


DJANGO_ROOT = Path(__file__).ancestor(3)
PROJECT_ROOT = DJANGO_ROOT.ancestor(1)
SITE_NAME = basename(PROJECT_ROOT)
CONFIGURATION_APP_ROOT = Path(__file__).ancestor(2)
PUBLIC_ROOT = PROJECT_ROOT.child('public')
path.append(DJANGO_ROOT)
path.append(CONFIGURATION_APP_ROOT)

SECRET_KEY = '7dcckq$8m2)mzwgu6&u#7+g4(3u#dl4k%9m9afpw+p-4!!!+ar'

DEBUG = True

TEMPLATE_DEBUG = True

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
)

LOCAL_APPS = (
    'images',
)

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'pipeline.middleware.MinifyHTMLMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'img.urls'

WSGI_APPLICATION = 'img.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'img.sqlite3'),
    }
}

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

TEMPLATE_DIRS = (
    DJANGO_ROOT.child('templates'),
)

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            'css/bootstrap.css',
            'css/project.css',
        ),
        'output_filename': 'css/base.css',
    },
}

PIPELINE_JS = {
    'base': {
        'source_filenames': (
            'js/jquery.js',
            'js/bootstrap.js',
        ),
        'output_filename': 'js/base.js',
    },
}
