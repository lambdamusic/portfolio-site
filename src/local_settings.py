import os
import sys
import django

SECRET_KEY = 'q*lq9&h*ln8qzzkos5@$!&*(asd67ta8dsjgportfolioapp'

# the django root is where django code lives
# the project root is one level up from src folder
# the site root is one level up from where manage.py is
DJANGO_ROOT = os.path.dirname(os.path.realpath(django.__file__))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 2)[0]
SITE_ROOT = os.path.dirname(os.path.realpath(__file__)).rsplit('/', 1)[0]

# Location: modify as needed
if "/michele.pasin/Dropbox/code/" in SITE_ROOT:
    ENVIRONMENT = 'local'
elif "/home/lambdaman/" in SITE_ROOT:
    ENVIRONMENT = 'pyany'
else:
    ENVIRONMENT = 'production'

print("Environment: %s" % ENVIRONMENT)

ALLOWED_HOSTS = [
    'localhost', '127.0.0.1', 'home.magicrebirth.webfactional.com',
    'ideaslab.magicrebirth.webfactional.com', 'magicrebirth.webfactional.com',
    'www.michelepasin.org', 'lambdaman.pythonanywhere.com'
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/media/static/'

# The STATIC_ROOT variable in settings.py defines the single folder you want to collect all your static files into (using ./manage.py collectstatic ).
if ENVIRONMENT == 'local':
    STATIC_ROOT = os.path.join(SITE_ROOT, 'collectstatic/portfolioapp')
else:
    #  webfaction => hardcoded into <media> APP
    STATIC_ROOT = "/home/magicrebirth/webapps/media/researcherapp"
    MEDIA_URL = 'http://www.michelepasin.org/upload/researcherapp/'
    STATIC_URL = 'http://www.michelepasin.org/media/researcherapp/'
    ADMIN_MEDIA_PREFIX = 'http://www.ichelepasin.org/media/researcherapp/admin/'

# This setting defines the additional locations the staticfiles app will traverse if the FileSystemFinder finder is enabled
STATICFILES_DIRS = (os.path.join(SITE_ROOT, 'src/static'), )

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

if ENVIRONMENT == 'local':

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'researcher2019',
            'USER': 'root',
            'PASSWORD': 'mikele',
            'HOST': '127.0.0.1',
            'PORT': '3306',
        }
    }

elif ENVIRONMENT == 'pyany':

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'lambdaman$researcher2019',
            'USER': 'lambdaman',
            'PASSWORD': '7df7698f',
            'HOST': 'lambdaman.mysql.pythonanywhere-services.com',
            'PORT': '3306',
        }
    }
else:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'researcher2019',
            'USER': 'magicrebirth_dem',
            'PASSWORD': '7df7698f',
            'HOST': '',
        }
    }
