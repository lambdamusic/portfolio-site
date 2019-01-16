# duplicate this file, rename as `local_settings.py` and fill in the settings according to your environment
# make sure you keep sensitive information private

import os
import sys
import django

SECRET_KEY = 'thedjangosecretkeyhere'

# the site root is one level up from where settings.py is
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
SITE_ROOT = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0]
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 2)[0]

# Location: modify as needed
if True:
    ENVIRONMENT = 'local'
else:
    ENVIRONMENT = 'production'

print("Environment: %s" % ENVIRONMENT)

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1', 'my.domain.heroku.com'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/media/static/'

# The STATIC_ROOT variable in settings.py defines the single folder you want to collect all your static files into (using ./manage.py collectstatic ).
if ENVIRONMENT == 'local':
    STATIC_ROOT = os.path.join(SITE_ROOT, 'collectstatic/path')
else:
    #  webfaction => hardcoded into <media> APP
    STATIC_ROOT = "/path/to/static/files"
    MEDIA_URL = 'http://static/files/'
    STATIC_URL = 'http://static/files/
    ADMIN_MEDIA_PREFIX = 'http://static/files/admin/'

# This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled
STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'src/static'), )

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if ENVIRONMENT == 'local':

    DATABASES = {
        'default': {
            'ENGINE': '',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
            'PORT': '',
        }
    }

else:

    DATABASES = {
        'default': {
            'ENGINE': '',
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
            'HOST': '',
        }
    }
