import os
from .settings import *  # noqa

VIRTUAL_HOST = os.getenv('VIRTUAL_HOST')
ALLOWED_HOSTS = [
    # For deploy
    VIRTUAL_HOST,
]

CSRF_TRUSTED_ORIGINS = [
    'https://' + VIRTUAL_HOST,
]

DEBUG = False

STATIC_ROOT = '/staticfiles/'

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
