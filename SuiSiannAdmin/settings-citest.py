from .settings import *  # noqa
from .settings import BASE_DIR
from os.path import join

SUISIANN_ROOT = join(BASE_DIR, 'taiuansuisiann')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}
