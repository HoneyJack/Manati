#
# Copyright (c) 2017 Stratosphere Lab.
# 
# This file is part of ManaTI Project 
# (see <https://stratosphereips.org>). It was created by 'Raul B. Netto <raulbeni@gmail.com>'
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public License
# along with this program. See the file 'docs/LICENSE' or see <http://www.gnu.org/licenses/> 
# for copying permission.
#
"""
Django settings for manati project.

Generated by 'django-admin startproject' using Django 1.9.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from decouple import config
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=True, cast=bool)
if DEBUG:
    print("Debug is enabled.")
    ALLOWED_HOSTS = ["127.0.0.1"]
else:
    ALLOWED_HOSTS = ["*"]

# Application definition
INSTALLED_APPS = [
    'django_rq',
    'guardian',
    'api_manager',
    'background_task',
    'rest_framework',
    'bootstrap3',
    'sass_processor',
    'django_extensions',
    'manati_ui.apps.ManatiUiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.staticfiles',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'manati.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'builtins':['manati_ui.templatetags.manati_ui_extras']
        },
    },
]


WSGI_APPLICATION = 'manati.wsgi.application'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': config('REDIS_PASSWORD'),
        'DEFAULT_TIMEOUT': 360,
        # 'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379/0'),  # If you're on Heroku
    },
    'high': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': config('REDIS_PASSWORD'),
        'DEFAULT_TIMEOUT': 360,
    },
    'low': {
        'HOST': 'localhost',
        'PORT': 6379,
        'DB': 0,
        'PASSWORD': config('REDIS_PASSWORD'),
        'DEFAULT_TIMEOUT': 360,
    }
}

RQ_SHOW_ADMIN_LINK = True





# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Prague'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

BACKGROUND_TASK_RUN_ASYNC = True # run the modules task, asynchronously
MAX_RUN_TIME = 20
MAX_ATTEMPTS = 3

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [ os.path.join(BASE_DIR, "static1"),]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

READ_ONLY_FILE = os.path.join(BASE_DIR, 'readonly')

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
IPYTHON_ARGUMENTS = [
    '--ext', 'django_extensions.management.notebook_extension',
]

NOTEBOOK_ARGUMENTS = [
    # exposes IP and port
    '--ip=0.0.0.0',
    '--port=8888',
    # disables the browser
    '--no-browser',
]

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend', # this is default
    'guardian.backends.ObjectPermissionBackend',
)
path_log_file = os.path.join(BASE_DIR, 'logs')
logfile_name = os.path.join(path_log_file, "server.log")
logfile_debug_name = os.path.join(path_log_file, "server_debug.log")

if not os.path.isfile(logfile_name):
    if not os.path.isdir(path_log_file):
        os.makedirs(path_log_file)
    f = open(logfile_name, "w")
    print('Creating file: ' + logfile_name)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        # "rq_console": {
        #     "format": "%(asctime)s %(message)s",
        #     "datefmt": "%H:%M:%S",
        # },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': logfile_name,
            'formatter': 'verbose',
            "maxBytes": 1024*1024*15,#15 MB
            "backupCount": 20,
            "encoding": "utf8"
        },
        # "rq_console": {
        #     "level": "DEBUG",
        #     "class": "rq.utils.ColorizingStreamHandler",
        #     "formatter": "rq_console",
        #     "exclude": ["%(asctime)s"],
        # },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        # "rq.worker": {
        #     "handlers": ["rq_console"],
        #     "level": "DEBUG"
        # },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"]
    }
}


GUARDIAN_GET_INIT_ANONYMOUS_USER = 'manati_ui.models.get_anonymous_user_instance'
ANONYMOUS_USER_ID = 1

if DEBUG:
    LOGGING['handlers']['file']['level'] = 'DEBUG'
    LOGGING['handlers']['file']['maxBytes'] = 1024*1024*30 # 30 MB
    LOGGING['handlers']['file']['filename'] = logfile_debug_name
    LOGGING['handlers']['console']['level'] = 'DEBUG'

    INTERNAL_IPS = ('127.0.0.1', 'localhost',)
    MIDDLEWARE_CLASSES += ['debug_toolbar.middleware.DebugToolbarMiddleware',]

    INSTALLED_APPS += ['debug_toolbar','pympler','template_profiler_panel']

    DEBUG_TOOLBAR_PANELS = [
           # 'djdt_flamegraph.FlamegraphPanel',
           'ddt_request_history.panels.request_history.RequestHistoryPanel',
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
           # 'pympler.panels.MemoryPanel',
           'template_profiler_panel.panels.template.TemplateProfilerPanel',
    ]

    # DEBUG_TOOLBAR_CONFIG = {
    #         'INTERCEPT_REDIRECTS': False,
    #         'SHOW_TOOLBAR_CALLBACK': 'ddt_request_history.panels.request_history.allow_ajax',
    #         'RESULTS_STORE_SIZE': 100,
    #    }