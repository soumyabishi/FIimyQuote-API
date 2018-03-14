from .settings import *

DEBUG = True
INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS += INTERNAL_IPS
ALLOWED_HOSTS.append('localhost')
#INSTALLED_APPS.append('debug_toolbar')
#MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': "django.db.backends.mysql",
        'NAME': "movie_quotes",
        'USER': "root",
        'PASSWORD': "",
        "HOST": "localhost",
        "PORT": "3306",
    }
}


