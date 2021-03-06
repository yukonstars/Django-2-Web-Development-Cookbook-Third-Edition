"""
Django settings for myproject project.

Generated by 'django-admin startproject' using Django 2.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _

from auth_extra.password_validation import (
    SpecialCharacterInclusionValidator)


USE_DJANGO_CRISPY_FORMS = False
CRISPY_TEMPLATE_PACK = 'bootstrap4'


# Build paths inside the project like this:
# os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(
    os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#l97f50r2m4ywrqp=!xn4vwadrr6@$19(2_2fp6vfw_ktfo@1a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if os.environ.get('DJANGO_USE_DEBUG'):
    DEBUG = True

ALLOWED_HOSTS = ['localhost']
if os.environ.get('SITE_HOST'):
    ALLOWED_HOSTS.append(os.environ.get('SITE_HOST'))


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.forms',
    'crispy_forms',
    'haystack',
    'sorl.thumbnail',
    'watermarker',
    'social_django',
    # local apps
    'artists',
    'bulletin_board',
    'custom_admin',
    'cv',
    'email_messages',
    'external_auth',
    'ideas',
    'likes',
    'locations',
    'magazine',
    'movies',
    'quotes',
    'products',
    'search',
    'utils',
]
if os.environ.get('DJANGO_USE_DEBUG_TOOLBAR'):
    INSTALLED_APPS += ('debug_toolbar',)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
if os.environ.get('DJANGO_USE_DEBUG_TOOLBAR'):
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',)


ROOT_URLCONF = 'myproject.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, "templates"),
    ],
    'APP_DIRS': True,
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.template.context_processors.i18n',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}]

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

if os.environ.get('MYSQL_HOST'):
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': os.environ.get('MYSQL_HOST'),
        'NAME': os.environ.get('MYSQL_DATABASE'),
        'USER': os.environ.get('MYSQL_USER'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD'),
    }


# Logging
# https://docs.djangoproject.com/en/dev/topics/logging/
LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/var/log/app.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    }
}

if DEBUG:
    # make all loggers use the console.
    for logger in LOGGING['loggers']:
        LOGGING['loggers'][logger]['handlers'] = ['console']


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTHENTICATION_BACKENDS = [
    'external_auth.backends.Auth0',
    'django.contrib.auth.backends.ModelBackend',
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
        'OPTIONS': {
            'max_similarity': 0.5,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 12,
        }
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
    {
        'NAME': 'auth_extra.password_validation.'
                'MaximumLengthValidator',
        'OPTIONS': {
            'max_length': 32,
        },
    },
    {
        'NAME': 'auth_extra.password_validation.'
                'SpecialCharacterInclusionValidator',
        'OPTIONS': {
            'special_chars': ('{', '}', '^', '&') +
                SpecialCharacterInclusionValidator.
                DEFAULT_SPECIAL_CHARACTERS
        }
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ("en", "English"),
    ("de", "Deutsch"),
    ("fr", "Français"),
    ("lt", "Lietuvių kalba"),
)

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'site_static'),
]
if os.environ.get('STATIC_HOST'):
    STATIC_DOMAIN = os.environ.get('STATIC_HOST')
    STATIC_URL = 'http://%s/' % STATIC_DOMAIN

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
if os.environ.get('MEDIA_HOST'):
    MEDIA_DOMAIN = os.environ.get('MEDIA_HOST')
    MEDIA_URL = 'http://%s/' % MEDIA_DOMAIN

UPLOAD_URL = f'{MEDIA_URL}upload/'
UPLOAD_ROOT = os.path.join(MEDIA_ROOT, 'upload')

# App settings

MAGAZINE_STATUS_CHOICES = (
    ("draft", _("Draft")),
    ("imported", _("Imported")),
    ("published", _("Published")),
    ("not_listed", _("Not Listed")),
    ("expired", _("Expired")),
)

HAYSTACK_CONNECTIONS = {
    'default_en': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_en'),
    },
    'default_de': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_de'),
    },
    'default_fr': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_fr'),
    },
    'default_lt': {
        'ENGINE': 'search.multilingual_whoosh_backend.'
                  'MultilingualWhooshEngine',
        'PATH': os.path.join(BASE_DIR, 'tmp/whoosh_index_lt'),
    },
}
HAYSTACK_CONNECTIONS['default'] = \
    HAYSTACK_CONNECTIONS[f'default_{LANGUAGE_CODE}']

MAPS_API_KEY = os.environ.get("MAPS_API_KEY")

SOCIAL_AUTH_AUTH0_DOMAIN = os.environ.get('AUTH0_DOMAIN')
SOCIAL_AUTH_AUTH0_KEY = os.environ.get('AUTH0_KEY')
SOCIAL_AUTH_AUTH0_SECRET = os.environ.get('AUTH0_SECRET')
SOCIAL_AUTH_AUTH0_SCOPE = ['openid', 'profile']
SOCIAL_AUTH_TRAILING_SLASH = False

LOGIN_URL = '/login/auth0'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'

CACHES = {
    'memcached': {
        'BACKEND': 'django.core.cache.backends.'
                   'memcached.MemcachedCache',
        'LOCATION': os.environ.get('CACHE_LOCATION',
                                   '127.0.0.1:11211'),
        "TIMEOUT": 60, # 1 minute
        "KEY_PREFIX": os.environ.get('CACHE_KEY',
                                     'myproject_production'),
    },
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': os.environ.get('CACHE_LOCATION',
                                   'redis://127.0.0.1:6379/1'),
        "TIMEOUT": 60, # 1 minute
        "KEY_PREFIX": os.environ.get('CACHE_KEY',
                                     'myproject_production'),
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        },
    },
}
CACHES['default'] = CACHES['memcached']
# or
# CACHES['default'] = CACHES['redis']
