# coding:utf8
"""
本番環境アプリ用設定ファイル
"""
from apps.settings.base import *

EMAIL_SUBJECT_PREFIX = "[{app_name}][production][{host}]".format(app_name=APP_CODE, host=socket.gethostname())

DEBUG = False
TEMPLATE_DEBUG = False

DOMAIN = "example.com"  #TODO

#TODO
DATABASES = { 
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '', 
        'PORT': '', 
    },  
}


#TODO
CACHES = {
    "default": {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': [
        ]
    },
}

IS_PRODUCTION = True

#TODO
SESSION_COOKIE_DOMAIN = ".example.com"
SESSION_COOKIE_SECURE = True

USE_SSL = True
