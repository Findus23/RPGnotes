"""
Django settings for rpg_notes project.

Generated by 'django-admin startproject' using Django 3.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
from datetime import timedelta
from pathlib import Path
from subprocess import run

import sentry_sdk
from django.utils.translation import gettext_lazy as _
from django_jinja.builtins import DEFAULT_EXTENSIONS
from django_tenants.files.storage import TenantFileSystemStorage
from sentry_sdk.integrations.django import DjangoIntegration

from .secrets import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

DOMAIN_WITH_DOT = "." + DOMAIN

ALLOWED_HOSTS = [DOMAIN_WITH_DOT]

# Application definition

DATABASE_ROUTERS = (
    'django_tenants.routers.TenantSyncRouter',
)
SHARED_APPS = (
    'django_tenants',  # mandatory
    'campaigns',  # you must list the app where your tenant model resides in
    'users',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'tenant_users.permissions',  # Defined in both shared apps and tenant apps
    'tenant_users.tenants',  # defined only in shared apps
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django_bootstrap5',
    'django_jinja',
    'django_jinja.contrib._humanize',
    'sorl.thumbnail',
    'debug_toolbar',
    'axes',
    'django_extensions',
    'django.contrib.postgres'
)

TENANT_APPS = (
    # The following Django contrib apps must be in TENANT_APPS
    'django.contrib.auth',  # Defined in both shared apps and tenant apps
    'django.contrib.contenttypes',  # Defined in both shared apps and tenant apps
    'tenant_users.permissions',  # Defined in both shared apps and tenant apps
    'django.contrib.admin',

    'locations',
    'characters',
    'loot',
    'days',
    'factions',
    'notes',
    'search',
    'graph',
    'pdf',
    'common',
    'simple_history',

)

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

TENANT_MODEL = "campaigns.Campaign"

TENANT_DOMAIN_MODEL = "campaigns.Domain"

TENANT_USERS_DOMAIN = DOMAIN

AUTH_USER_MODEL = 'users.TenantUser'

AUTHENTICATION_BACKENDS = (
    'axes.backends.AxesBackend',
    'tenant_users.permissions.backend.UserBackend',
)

SESSION_COOKIE_DOMAIN = DOMAIN_WITH_DOT

DEFAULT_FILE_STORAGE = "django_tenants.files.storage.TenantFileSystemStorage"

MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middlewares.AuthMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',
    'csp.middleware.CSPMiddleware',
    'axes.middleware.AxesMiddleware'
]

ROOT_URLCONF = 'rpg_notes.urls'
PUBLIC_SCHEMA_URLCONF = 'rpg_notes.urls_public'

TEMPLATES_DIR = BASE_DIR / 'templates'
TEMPLATES = [
    {
        "BACKEND": "django_jinja.backend.Jinja2",
        "DIRS": [TEMPLATES_DIR],
        "APP_DIRS": True,
        "OPTIONS": {
            # "extensions": DEFAULT_EXTENSIONS + [
            # 'jdj_tags.extensions.DjangoCompat',
            # ]
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.contrib.messages.context_processors.messages',
            ],
            "bytecode_cache": {
                "name": "default",
                "backend": "django_jinja.cache.BytecodeCache",
                "enabled": True,
            },
        }
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'rpg_notes.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('de', _('German')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / "locale"
]

TIME_ZONE = 'Europe/Vienna'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

SHELL_PLUS = "bpython"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

THUMBNAIL_ALTERNATIVE_RESOLUTIONS = [2, 3]

ACCOUNT_ACTIVATION_DAYS = 7  # One-week activation window

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = "[RPGnotes]"

CSP_DEFAULT_SRC = ["'self'", 'data:', "https://bugs.lw1.at"]
CSP_SCRIPT_SRC = ["'self'", "https://bugs.lw1.at"]
CSP_WORKER_SRC = ["'self'", "blob:"]
CSP_STYLE_SRC = ["'self'", "'unsafe-inline'"]
CSP_REPORT_ONLY = DEBUG
if DEBUG:
    CSP_EXCLUDE_URL_PREFIXES = ("/")
if SENTRY_CSP_REPORT_URI:
    CSP_REPORT_URL = SENTRY_CSP_REPORT_URI
CSP_FRAME_ANCESTORS = ["'none'"]
CSP_INCLUDE_NONCE_IN = ['script-src']

THUMBNAIL_KVSTORE = "sorl.thumbnail.kvstores.redis_kvstore.KVStore"
redis_url = "redis://127.0.0.1:6379/9" if DEBUG else "unix:///var/run/redis-rpgnotes/redis-server.sock?db=2"
THUMBNAIL_REDIS_URL = redis_url.replace("?db=2", "?db=1")
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": redis_url,
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
}

SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
SESSION_CACHE_ALIAS = "default"
SESSION_COOKIE_AGE = 60 * 60 * 24 * 30 * 2

THUMBNAIL_DEBUG = DEBUG
THUMBNAIL_PRESERVE_FORMAT = True

if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

    AXES_IPWARE_META_PRECEDENCE_ORDER = ['HTTP_X_REAL_IP']
    AXES_COOLOFF_TIME = timedelta(hours=1)
    AXES_FAILURE_LIMIT = 6

    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.ManifestStaticFilesStorage"
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': 'DEBUG',
                'class': 'logging.FileHandler',
                'filename': '/srv/server/rpgnotes/app.log',
            },
        },
        'loggers': {
            'django': {
                'handlers': ['file'],
                'level': 'INFO',
                'propagate': True,
            },
        },
    }
    if SENTRY_DSN:
        sp = run(["git", "rev-parse", "--verify", "HEAD"], capture_output=True)
        commit = sp.stdout.decode().strip()

        sentry_sdk.init(
            dsn=SENTRY_DSN,
            integrations=[DjangoIntegration()],
            auto_session_tracking=False,
            traces_sample_rate=0.01,
            release=commit
        )
