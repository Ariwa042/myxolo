"""
Django settings for xolo project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-wu70r19c=ua@4!js2gijsibhr$bq&6k!$5=nym2ojk1wuz1=(g'
AUTH_USER_MODEL = 'account.User'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = ['https://localhost:8000']

# Application definition

INSTALLED_APPS = [
    'account',
    'core',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'jazzmin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
  #  'whitenoise.middleware.WhiteNoiseMiddleware',  # 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'xolo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'xolo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static'),  # Ensure this points to your development static files
]

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# settings.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_PORT = 587
#EMAIL_USE_TLS = True
#EMAIL_HOST_USER = 'escrowtrade02@gmail.com'  # Replace with your Gmail address
#EMAIL_HOST_PASSWORD = 'lkeb fkzs dofo qxtp' # Your Gmail app password
EMAIL_TIMEOUT = 60
EMAIL_BACKENDS = {
    'AIRDROP': {
        'EMAIL_HOST': 'smtp.gmail.com',
        'EMAIL_PORT': 587,
        'EMAIL_HOST_USER': 'escrowtrade02@gmail.com',
        'EMAIL_HOST_PASSWORD': 'lkeb fkzs dofo qxtp',
        'EMAIL_USE_TLS': True,
          # Timeout in seconds

    },
    'GIVEAWAY': {
        'EMAIL_HOST': 'smtp.gmail.com',
        'EMAIL_PORT': 587,
        'EMAIL_HOST_USER': 'escrowtrade02@gmail.com',
        'EMAIL_HOST_PASSWORD': 'lkeb fkzs dofo qxtp',
        'EMAIL_USE_TLS': True,
    },
    'REFUND': {
        'EMAIL_HOST': 'smtp.gmail.com',
        'EMAIL_PORT': 587,
        'EMAIL_HOST_USER': 'Coin Tracker cointracker.llc@gmail.com',
        'EMAIL_HOST_PASSWORD': 'lmpp zwmt ogxd wjik',
        'EMAIL_USE_TLS': True,
    },
}

#JAZZMIN SETUP
