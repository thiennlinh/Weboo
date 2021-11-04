"""
Django settings for root project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from datetime import timedelta

from rest_framework import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$7=(j$^7hz-)^ty43gd@^bmkpjy!uf-$++6a+ybpz6e-(l8h=&'

# Stripe
STRIPE_PUB_KEY = 'pk_test_51JruriCfgBBzOco65hm5ue6YfP2gwhaXP5cGTYIXtRCpUicgVTBAOpRDShc6t91E86knP2PhL2gW5JyrUPkatNrJ00PRvTFVS7'
STRIPE_SECRET_KEY = 'sk_test_51JruriCfgBBzOco65DnDtPQm5k4oWdClRX5Q1w2EoezoACB8zDYUnSedZ9KU8YPsyVlgcKkn9XnPa5nAyiye8H2H00YwhxryIz'

STRIPE_PRICE_ID_MEMBER_MONTH = 'price_1Js9SOCfgBBzOco6DqJ5aaj0'
STRIPE_PRICE_ID_MEMBER_VIP = 'price_1Js9UeCfgBBzOco6XtwW76Hm'

STRIPE_WEBHOOK_KEY = 'whsec_iV0qP1UMZEvR53tkDW7rGBE6EgFZ6sxj'

# SECURITY WARNING: don't run with debug turned on in production!
ENVIRONMENT = os.environ.get("APPS_ENVIRONMENT")
if ENVIRONMENT == 'prod':
    DEBUG = False
    ALLOWED_HOSTS = ['*']
else:
    DEBUG = True
    ALLOWED_HOSTS = ['*']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'root.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=14),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'AUTH_HEADER_TYPES': ('JWT',),
}

AUTH_USER_MODEL = 'auth.User'

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/
from django.utils.translation import gettext_lazy as _

LANGUAGE_CODE = 'vi-VI'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
   os.path.join(BASE_DIR, 'locale'),
   os.path.join(BASE_DIR, 'polls/locale')
)

LANGUAGES = (
    ('vi', _('Vietnamese')),
    ('en', _('English')),
)

MULTILINGUAL_LANGUAGES = (
    "en-us",
    "vi",
)

AUTH_KEYS_DIR = '%s/root/settings/auth_key' % BASE_DIR

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", "media")
FILEBROWSER_MEDIA_ROOT = MEDIA_ROOT
FILEBROWSER_DIRECTORY = '/uploads/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static", "root")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", "static"),
)
