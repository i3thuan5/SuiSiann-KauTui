from .settings import *  # noqa
from .settings import BASE_DIR
from os.path import join

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(BASE_DIR, 'db.sqlite3'),
    }
}
