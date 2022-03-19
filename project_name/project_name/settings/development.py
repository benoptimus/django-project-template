"""Development settings and globals."""


from os.path import join, normpath

from .base import *

from utilities import helpers

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
TEMPLATE_STRING_IF_INVALID = '' #'%s'
########## END DEBUG CONFIGURATION

# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["18.224.5.252", "localhost",]

########## EMAIL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = helpers.get_env_setting('EMAIL_HOST')
EMAIL_PORT = helpers.get_env_setting('EMAIL_PORT')
EMAIL_HOST_USER = helpers.get_env_setting('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = helpers.get_env_setting('EMAIL_HOST_PASSWORD')
EMAIL_SUBJECT_PREFIX = '[%s] ' % SITE_NAME
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
########## END EMAIL CONFIGURATION

########## END EMAIL CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': helpers.get_env_setting('DATABASE_NAME'),
		'USER':  helpers.get_env_setting('MYSQL_USER'),
		'PASSWORD': helpers.get_env_setting('MYSQL_PASSWORD'),
		'HOST': helpers.get_env_setting('DATABASE_HOST'),
		'PORT': helpers.get_env_setting('DATABASE_PORT'),
	}
}
########## END DATABASE CONFIGURATION

########## PAGINATION CONFIGURATION
PAGINATION_SETTINGS = {
	'PAGE_RANGE_DISPLAYED': 10,
		'MARGIN_PAGES_DISPLAYED': 2,
		}

########## CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
	'default': {
		'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
	}
}
########## END CACHE CONFIGURATION

APPEND_SLASH = False
