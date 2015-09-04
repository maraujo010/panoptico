"""
Django settings for panoptico project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2--k)7c4%^zr^xid1sy6o0)7xqdj)&$27^k!)qimzp)tsj(-*_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis', 
    'panoptico.apps.webApp',
    'panoptico.apps.mobileApp',
    'panoptico.apps.webservices'
,)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'panoptico.apps.webApp.middleware.AutoLogout', 
)

AUTH_USER_MODEL = 'webApp.PanopticoUser'

ROOT_URLCONF = 'panoptico.urls'

WSGI_APPLICATION = 'panoptico.wsgi.application'


SESSION_EXPIRE_AT_BROWSER_CLOSE = True

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'

AUTO_LOGOUT_DELAY = 60


DATABASES = {
    'default': {        
        'ENGINE': 'django.db.backends.postgresql_psycopg2', 
        'NAME': 'panoptico',         
        'USER': '*',
        'PASSWORD': '*',
        'HOST': 'localhost',
        'PORT': '',                 
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'pt-PT'

TIME_ZONE = 'Europe/Lisbon'

USE_I18N = False

USE_L10N = True

USE_TZ = True


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))


TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates/',
)

TEMPLATE_DEBUG = False
