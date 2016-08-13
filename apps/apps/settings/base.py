# coding:utf8
"""
全環境で最初にimportされるファイル
"""
import os
import socket

APP_CODE = "etoki"
APP_LABEL = u"etoki"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
EMAIL_SUBJECT_PREFIX = "[{app_name}][local][{host}]".format(app_name=APP_CODE, host=socket.gethostname())

###############################
# 環境特有の設定
###############################
DEBUG = True

ADMINS = (
)
MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', 
        'NAME': os.path.join(BASE_DIR, "{0}.db".format(APP_CODE)),
        'USER': '',
        'PASSWORD': '', 
        'HOST': '',
        'PORT': '',
    }
}

CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/{0}.cache'.format(APP_CODE),
        "TIMEOUT": 60,
        "KEY_PREFIX": "default",
        "OPTIONS": {
            "MAX_ENTRIES": 10000000,
        }
    },
}


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'formatters': {
        'standard': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'app': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/app.log',
            'maxBytes': 1024 * 1024 * 50,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'app': {
            'handlers': ['app'],
            'level': 'INFO',
            'propagate': True,
        },
    }
}

# 本番環境かどうか
IS_PRODUCTION = False

# ドメイン
DOMAIN = "127.0.0.1:8000"

###############################
# 環境共通の設定
###############################
TIME_ZONE = "Asia/Tokyo"
LANGUAGE_CODE = "ja"
SITE_ID = 1
USE_I18N = True
USE_L10N = False
USE_TZ = False

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
STATIC_ROOT = ''
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
SECRET_KEY = 'FG6dfshchVyBp2vbA2UnkYH4kGhuCJiasd3DDFa3'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                "django.template.context_processors.csrf",
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "apps.core.context_processors.core",
            ],
        },
    },
]


MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'apps.urls'
WSGI_APPLICATION = 'apps.wsgi.application'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.humanize',
    'apps.core',
    'apps.account',
    'apps.enquete',
)

SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_COOKIE_AGE = 60*60*24*30 #30日間
DEFAULT_LOCALE = "ja_JP.UTF-8"

ALLOWED_HOSTS = ["*"]

LOGIN_URL = "/account/login"
LOGIN_REDIRECT_URL = "/account/mypage/"

ATOMIC_REQUESTS = True

USER_SESSION_KEY = "user_session_key"

EMAIL_FROM = "no-reply@example.com"

USE_SSL = False
