from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# INSTALLED_APPS += ["debug_toolbar", ]

LLOWED_HOSTS = ['localhost', '127.0.0.1']

MIDDLEWARE_CLASSES += (
    'middleware.profile.ProfilerMiddleware',
)

PAGE_SIZE = 2

SECRET_KEY = ['gfdgbdfgdfgd']
