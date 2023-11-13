import os
from .settings import *  # noqa
from .settings import INSTALLED_APPS, MIDDLEWARE
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

VIRTUAL_HOST = os.getenv('HOKBU_DOMAIN_NAME')

ALLOWED_HOSTS = [
    # For deploy
    VIRTUAL_HOST,
]

CSRF_TRUSTED_ORIGINS = [
    'https://' + VIRTUAL_HOST,
]

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = False

STATIC_ROOT = '/staticfiles/'

INSTALLED_APPS += [
    'axes',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'ithuan',
        'HOST': 'postgres',
        'PORT': '',
    }
}

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesStandaloneBackend',
    'django.contrib.auth.backends.ModelBackend',
]

MIDDLEWARE += [
    'axes.middleware.AxesMiddleware',
]

AWS_S3_USE_SSL = True
AWS_S3_SIGNATURE_VERSION = 's3v4'


SENTRY_DSN = os.getenv('SENTRY_DSN')
if SENTRY_DSN:
    sentry_sdk.init(
        dsn=SENTRY_DSN,
        integrations=[DjangoIntegration()],

        # Set traces_sample_rate to 1.0 to capture 100%
        # of transactions for performance monitoring.
        # We recommend adjusting this value in production.
        traces_sample_rate=0.1,

        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data.
        send_default_pii=True
    )
