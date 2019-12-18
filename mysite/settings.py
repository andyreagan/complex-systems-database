"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# for django-cms
gettext = lambda s: s
PROJECT_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('DJ_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DJ_DEBUG') in ['TRUE','1','true','True']
 
TEMPLATE_DEBUG = DEBUG

TEMPLATE_DIRS = [os.path.join(BASE_DIR,'templates')]

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    # 'cms.context_processors.cms_settings',
    # "sekizai.context_processors.sekizai",
)

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)

ALLOWED_HOSTS = [
    '.uvm.edu',
    '.uvm.edu.',
    '.hedonometer.org',
    '.hedonometer.org.',
]

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    # 'cms',  # django CMS itself
    # 'mptt',  # utilities for implementing a modified pre-order traversal tree
    # 'menus',  # helper for model independent hierarchical website navigation
    # 'sekizai',  # for javascript and css management
    # 'djangocms_admin_style',  # for the admin skin. You **must** add 'djangocms_admin_style' in the list before 'django.contrib.admin'.
    'suit',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cmplxsys',
    'django.contrib.humanize',
    'south',
    'tastypie',
    'corsheaders',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    # an attempt to try to control CORS
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # this doesn't allow iframes from our site
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # for django cms
    # 'django.middleware.locale.LocaleMiddleware',
    # 'django.middleware.doc.XViewMiddleware',
    # 'cms.middleware.page.CurrentPageMiddleware',
    # 'cms.middleware.user.CurrentUserMiddleware',
    # 'cms.middleware.toolbar.ToolbarMiddleware',
    # 'cms.middleware.language.LanguageCookieMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': os.getenv('DJ_DB_ENGINE'),
#         'NAME': os.getenv('DJ_DB_NAME'),
#         'USER': os.getenv('DJ_DB_USER'),
#         'PASSWORD': os.getenv('DJ_DB_PASSWORD'),
#         'HOST': os.getenv('DJ_DB_HOST'),
#         'PORT': os.getenv('DJ_DB_PORT'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'CMPLXSYS_django',
        'USER': 'cmplxsys_admin',
        # 'PASSWORD': 'wkNsvp76IFEajWzX',
        'PASSWORD': 'vgkKEN7JSfH1',
        'HOST': 'webdb.uvm.edu',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/New_York'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.getenv('DJ_STATIC_ROOT')
# export DJ_STATIC_ROOT=/users/c/m/cmplxsys/www-root/static

MEDIA_URL = '/static/media/'
MEDIA_ROOT = '/users/c/m/cmplxsys/www-root/static/media/'

SOUTH_MIGRATION_MODULES = {
'default': 'cmplxsys.default.south_migrations',
}

# from http://ianalexandr.com/blog/getting-started-with-django-logging-in-5-minutes.html
# settings.py
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'mysite.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'DEBUG',
#         },
#         'hedonometer': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#         },
#     }
# }
