"""
Django settings for ira_web project.

Generated by 'django-admin startproject' using Django 4.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-1a$8)6sn)li6^@8qke)-i8rd@^d=+j622g+u5@wgjfn+#9#rh3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'guesthouse.apps.GuesthouseConfig',
    'crispy_forms',
    'members',
    'stage.apps.StageConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ira_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ira_web.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
#DATABASE_ROUTERS = ["stage.routers.StageRouter", "guesthouse.router.AllRouter", "members.router.AllRouter"]
DATABASE_ROUTERS = ['ira_web.router.AuthRouter','ira_web.router.Host','ira_web.router.Stage']

#DATABASE_APPS_MAPPING = {'guesthouse':'host', 'stage': 'stage', 'members':'host'}
DATABASES = {
    'default': {},
    'auth_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_auth',
        'USER': 'root',
        'PASSWORD': 'iraapps01',
        'HOST': '192.168.12.125',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"}
    },

    'host':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'irahost',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'USER': 'root',
        'PASSWORD': 'iraapps01',
        'HOST': '192.168.12.125',
        'PORT': '3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    },
   
    'stage': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "stage",
        "USER": "root",
        "PASSWORD": "iraapps01",
        "HOST": "192.168.12.125",
        "PORT": "3306",
        'OPTIONS': { 'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"},
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

#AUTH_USER_MODEL = "guesthouse.CustomUser"

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Tunis'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
