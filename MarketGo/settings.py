"""
python
import pymysql
pymysql.install_as_MySQLdb()
Django settings for MarketGo project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import pymysql

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s(n2-67i+zk8po6hh#7xe0#eke9rbb*(#mq*!q_u2n%9_-$nqd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
LOGIN_URL= "core:login"

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'marketgo.local']



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'product',
    'cart',
    'core',
    'checkout',

    # Third Party Apps
    'paypal.standard.ipn',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'cart.apps.CartConfig',
]

ROOT_URLCONF = 'MarketGo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'MarketGo' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart'
            ],
        },
    },
]

WSGI_APPLICATION = 'MarketGo.wsgi.application'



# Use database-backed sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.db'
# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
pymysql.install_as_MySQLdb()



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'marketgo_db',
        'USER': 'marketgo_user',
        'PASSWORD': 'marketgo_pass',
        'HOST': 'db',  # Correspond au nom du service dans docker-compose.yml
        'PORT': '3306',
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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
# Add these new lines
STATICFILES_DIRS = [BASE_DIR / "static"]



STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')



DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_SESSION_ID = 'cart'






PAYPAL_RECEIVER_EMAIL = 'sb-479wt4329368047@business.example.com'
PAYPAL_TEST= True