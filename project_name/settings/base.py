"""Common settings and globals."""

from logging.handlers import SysLogHandler
from os.path import abspath, basename, dirname, join, normpath
from sys import path
from datetime import timedelta

########## PATH CONFIGURATION
# Absolute filesystem path to the Django project directory:
DJANGO_ROOT = dirname(dirname(abspath(__file__)))

# Absolute filesystem path to the top-level project folder:
SITE_ROOT = dirname(DJANGO_ROOT)

#setting base_dir for django_extensions
BASE_DIR = SITE_ROOT

# Site name:
SITE_NAME = basename(DJANGO_ROOT)

# Add our project to our pythonpath, this way we don't need to type our project
# name in our dotted import paths:
path.append(DJANGO_ROOT)
########## END PATH CONFIGURATION

########## DEBUG CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = False

# See: https://docs.djangoproject.com/en/dev/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG
########## END DEBUG CONFIGURATION


########## MANAGER CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
ADMINS = (
	('Your Name', 'your_email@example.com'),
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = ADMINS
########## END MANAGER CONFIGURATION


########## DATABASE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
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
########## END DATABASE CONFIGURATION


########## GENERAL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = 'Africa/Dakar'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = 'fr-FR'

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True
########## END GENERAL CONFIGURATION


########## MEDIA CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-root
MEDIA_ROOT = normpath(join(SITE_ROOT, 'media'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#media-url
MEDIA_URL = '/media/'
########## END MEDIA CONFIGURATION


########## STATIC FILE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = normpath(join(SITE_ROOT, 'assets'))

# See: https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = '/static/'

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
	normpath(join(SITE_ROOT, 'static')),
)

# See: https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
########## END STATIC FILE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = 'django-insecure-l%_e__(qtw2ov0m#$#382zpxgj4jbkkt&ai)k8!#)5ne#21ym&'
########## END SECRET CONFIGURATION


########## FIXTURE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-FIXTURE_DIRS
FIXTURE_DIRS = (
	normpath(join(SITE_ROOT, 'fixtures')),
)
########## END FIXTURE CONFIGURATION


########## TEMPLATE CONFIGURATION
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(SITE_ROOT, 'templates')),
        ],
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.contrib.auth.context_processors.auth',
				'django.template.context_processors.debug',
				'django.template.context_processors.i18n',
				'django.template.context_processors.media',
				'django.template.context_processors.static',
				'django.template.context_processors.tz',
				'django.contrib.messages.context_processors.messages',
				'django.template.context_processors.request',
            ],
			'loaders': [
                'django.template.loaders.filesystem.Loader',
				'django.template.loaders.app_directories.Loader',
            ]
        },
    },
]
########## END TEMPLATE CONFIGURATION

LOCALE_PATHS   = (
	normpath(join(SITE_ROOT, 'locale')),
)

########## MIDDLEWARE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#middleware-classes
MIDDLEWARE = (
	'corsheaders.middleware.CorsMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.locale.LocaleMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
)
########## END MIDDLEWARE CONFIGURATION


########## URL CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = '%s.urls' % SITE_NAME
########## END URL CONFIGURATION


########## APP CONFIGURATION
DJANGO_APPS = (
	# Default Django apps:
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django.contrib.admin',

	# Useful template tags:
	#'django.contrib.humanize',
	# Admin panel and documentation:
	#'django.contrib.admindocs',
	)

THIRD_PARTY_APPS = (
    'corsheaders',
    'django_extensions',
    'rest_framework',
    'rest_framework_simplejwt',
    #'drf_yasg',
    'drf_spectacular',
    'drf_spectacular_sidecar',
	)

# Apps specific for this project go here.
LOCAL_APPS = (
	"cuser",
 	"api",
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
########## END APP CONFIGURATION


########## LOGGING CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#logging
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
	'version': 1,
	'disable_existing_loggers': False,
	'filters': {
		'require_debug_false': {
			'()': 'django.utils.log.RequireDebugFalse'
		}
	},
	'formatters': {
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
		'console':{
			'level':'DEBUG',
			'class':'logging.StreamHandler',
			'formatter': 'verbose'
		},
		'syslog': {
			'level':'DEBUG',
			'class':'logging.handlers.SysLogHandler',
			'formatter': 'verbose',
			'facility': SysLogHandler.LOG_LOCAL2,
		},
	},
	'loggers': {
		'django.request': {
			'handlers': ['mail_admins'],
			'level': 'ERROR',
			'propagate': True,
		},
		   '{{ project_name }}': {
			'handlers': ['console', 'syslog'],
			'level': 'DEBUG',
			'propagate': True,
		},
	}
}
########## END LOGGING CONFIGURATION


########## WSGI CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = 'wsgi.application'
########## END WSGI CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'cuser.User'
########## END AUTH_USER_MODEL CONFIGURATION

#AUTH_PROFILE_MODULE = ''

#AUTHENTICATION_BACKENDS
AUTHENTICATION_BACKENDS = ['{{ project_name }}.auth.backends.EmailBackend']

#SOUTH
SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False


#PICTURE_UPLOAD_DIR = '/tmp/'

#ISSUE_TRACKER_URL = ''

DATE_INPUT_FORMATS = (
	'%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y',
	'%b %d %Y', '%b %d, %Y',
	'%d %b %Y', '%d %b, %Y',
	'%B %d %Y', '%B %d, %Y',
	'%d %B %Y', '%d %B, %Y',
)

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES':(
        'utilities.renderers.CustomRenderer',
    ),
    'EXCEPTION_HANDLER': 'utilities.renderers.custom_exception_handler',
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = False

CORS_ALLOWED_ORIGINS = [
]

APPEND_SLASH = False

SWAGGER_SETTINGS = {
   'SECURITY_DEFINITIONS': {
      'Basic': {
            'type': 'basic'
      },
      'Token': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
      }
   }
}


SPECTACULAR_SETTINGS = {
    'TITLE': '{{ project_name }} API',
    'DESCRIPTION': 'APP',
    'VERSION': 'V1',
    #'SWAGGER_UI_DIST': 'SIDECAR',  # shorthand to use the sidecar instead
    #'SWAGGER_UI_FAVICON_HREF': 'SIDECAR',
    #'REDOC_DIST': 'SIDECAR',

    #'SERVE_URLCONF':'http://localhost:8000/swagger?format=openapi',
    'SERVERS': [{'url':'http://localhost:8000', 'description':'dev'}],
    'SERVE_INCLUDE_SCHEMA': False,
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=2),
    'ROTATE_REFRESH_TOKENS': False,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': False,

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=5),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}
