from .base import *


########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
here = lambda * x: join(DJANGO_ROOT, *x)
PROJECT_ROOT = here("..")
TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT
TEST_DISCOVER_ROOT = PROJECT_ROOT
TEST_DISCOVER_PATTERN = "*"
########## IN-MEMORY TEST DATABASE

DATABASES = {
	"default": {
		"ENGINE": "django.db.backends.sqlite3",
		"NAME": ":memory:",
		"USER": "",
		"PASSWORD": "",
		"HOST": "",
		"PORT": "",
}, }

LANGUAGE_CODE = 'en'
