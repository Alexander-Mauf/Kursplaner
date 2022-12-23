"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
BASE_URL = 'http://0.0.0.0:8000'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'DEV-KEY')

# hashfield
# https://github.com/nshafer/django-hashid-field
HASHID_FIELD_SALT = os.environ.get('HASH_FIELD_SALT', 'BY,N`~e@f)cUL6b[dWL_wT;#|}LCrsav')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEST_MODE = True

if os.environ.get("TEST_MODE", "True") == "False":
    TEST_MODE = False

ALLOWED_HOSTS = []

LOGIN_URL = '/admin/login/'

LOGIN_REDIRECT_URL = '/admin/login/'

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd Party
    'django_filters',
    'rest_framework',
    'crispy_forms',
    # own
    'kurse',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "kursplaner.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ("django_filters.rest_framework.DjangoFilterBackend",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
    ),
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    },
}

WSGI_APPLICATION = "kursplaner.wsgi.application"

PLUGINS = {
    "ACCOUNTING": {
        'STATSDISPLAYS': {
            'INSTALLED': [
                "FOOBAR_V1",
                "BIGQUERY_TABLE_V1",
                "GRAPHIC_BRANCH_USER_STATS_V1",
            ]
        },
    },
}

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('DATABASE_NAME_DB', 'kursplaner'),
        'USER': os.environ.get('DATABASE_USER_DB', 'root'),
        'PASSWORD': os.environ.get('DATABASE_PWD_DB', 'semaphoredb'),
        'HOST': os.environ.get('DATABASE_HOST_DB', '0.0.0.0'),
        'PORT': os.environ.get('DATABASE_HOST_PORT', '3306'),
        "OPTIONS": {
            # Tell MySQLdb to connect with 'utf8mb4' character set
            'charset': 'utf8mb4',
            'use_unicode': True,
        },
    }
}

GID = {
    "APP_NAME": "skischule-fichtelberg-kursplaner",
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

X_FRAME_OPTIONS = 'ALLOW'

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "de-de"

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # other finders..
)

STATICFILES_DIRS = (
    os.path.join(os.path.dirname(__file__), '..', 'node_modules'),
)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Versionierung der Signing-Keys
SIGNING_VERSION_MIN = os.environ.get('SIGNING_VERSION_MIN', 1)

if DEBUG:
    ALLOWED_HOSTS += ('*',)
    INTERNAL_IPS = ('127.0.0.1', 'localhost', '0.0.0.0:8000')
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    )
    INSTALLED_APPS += (
        'debug_toolbar',
    )
    DEBUG_TOOLBAR_PANELS = [
        'debug_toolbar.panels.versions.VersionsPanel',
        'debug_toolbar.panels.timer.TimerPanel',
        'debug_toolbar.panels.settings.SettingsPanel',
        'debug_toolbar.panels.headers.HeadersPanel',
        'debug_toolbar.panels.request.RequestPanel',
        'debug_toolbar.panels.sql.SQLPanel',
        'debug_toolbar.panels.staticfiles.StaticFilesPanel',
        'debug_toolbar.panels.templates.TemplatesPanel',
        'debug_toolbar.panels.cache.CachePanel',
        'debug_toolbar.panels.signals.SignalsPanel',
        'debug_toolbar.panels.logging.LoggingPanel',
        'debug_toolbar.panels.redirects.RedirectsPanel',
    ]

    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': False,
        'SHOW_COLLAPSED': True
    }

if (os.environ.get('ENV', 'develop')) == 'production':
    DEBUG = False
    TEST_MODE = os.environ.get("TEST_MODE", False)
    ALLOWED_HOSTS += ('+.ey.r.appspot.com',)
    BASE_URL = os.environ.get('BASE_URL', "")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.environ.get('DATABASE_NAME'),
            'USER': os.environ.get('DATABASE_AUTH_USER'),
            'PASSWORD': os.environ.get('DATABASE_AUTH_PWD'),
            'HOST': os.environ.get('DATABASE_HOST_DB'),
            'PORT': os.environ.get('DATABASE_HOST_PORT'),
        }
    }

    # Security
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_SAMESITE = 'None'
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_SAMESITE = 'None'  # As a string
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    ## that requests over HTTP are redirected to HTTPS. aslo can config in webserver
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTOCOL", "https")
    ## X-Frame-Options
    X_FRAME_OPTIONS = 'DENY'
    ## Strict-Transport-Security
    SECURE_HSTS_SECONDS = 15768000
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SESSION_COOKIE_AGE = 3 * 24 * 60 * 60  # 3 Days of session Cookie
    SESSION_EXPIRE_AT_BROWSER_CLOSE = False



BOOTSTRAP5 = {
    "css_url": {
        "url": f"{BASE_URL}/static/bootstrap/dist/css/bootstrap.min.css",
        "crossorigin": "anonymous",
    },
    "javascript_url": {
        "url": f"{BASE_URL}/static/bootstrap/dist/js/bootstrap.bundle.min.js",
        "crossorigin": "anonymous",
    },
    'server_side_validation': False,
}

FILTERS_EMPTY_CHOICE_LABEL = ''
