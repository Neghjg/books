"""
Django settings for books_site project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-j(ret1l-%#74gh83@o-9e)di4r5wcf7i++0einpnndev)amj^@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'mysite.com', 'bookingcom.pythonanywhere.com']

SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    'social_django',
    'django_extensions',
    'books.apps.BooksConfig',
    'authorization.apps.AuthorizationConfig',
    "debug_toolbar",
    'cart',
    'orders',
    'mathfilters',
    'huey.contrib.djhuey',
    'django_recaptcha',
    'taggit',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'payment.apps.PaymentConfig',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',
]

REST_FRAMEWORK = {
    #'DEFAULT_PERMISSION_CLASSES': [
    #    'rest_framework.permissions.IsAuthenticatedOrReadOnly'
    #],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        
    ],
    #'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    #'PAGE_SIZE': 20,
}


AUTHENTICATION_BACKENDS = [
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.vk.VKOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'authorization.authentication.EmailAuthBackend',
]

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# Для PostgreSQL
SOCIAL_AUTH_JSONFIELD_ENABLED = True

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '49411574675-o4g7cnrnsg8c2febdaon0ff1skl9b4rr.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_VK_OAUTH2_KEY = '51783810'
SOCIAL_AUTH_VK_OAUTH2_SECRET = '5pfJJqMTtliZjflzypME'

SOCIAL_AUTH_VK_OAUTH2_SCOPE = ["email"]
SOCIAL_AUTH_VK_OAUTH2_EXTRA_DATA = ['first_name', 'last_name']
SOCIAL_AUTH_VK_APP_USER_MODE = 1

LOGIN_REDIRECT_URL = '/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'books_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'orders.context_processors.get_user_orders',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'books_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# For sqllite
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

# For Postgresql
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bookingcom',
        'USER': 'bookingcom',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
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

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_SESSION_ID = 'cart'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# Яндекс
#EMAIL_HOST = 'smtp.yandex.ru'
#EMAIL_HOST_USER = 'jovannymoriarty@yandex.ru'
#EMAIL_HOST_PASSWORD = 'zmcjnykyitsuyscr' 
#EMAIL_PORT = 465
#EMAIL_USE_SSL = True
#EMAIL_USE_TLS = False
# Google
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = "neghjg17@gmail.com"
EMAIL_HOST_PASSWORD = "rkbhrodpeijlkrud"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

HUEY = {
    "name": "mydjangoproject",
    "url": "redis://localhost:6379/?db=1",
}

HUEY["immediate_use_memory"] = False
HUEY["immediate"] = False

INTERNAL_IPS = [
    "127.0.0.1",
]


RECAPTCHA_PUBLIC_KEY = '6LdRyD4pAAAAAIQPWTzrlzfdFnJq1ni3zJFDaTQW'
RECAPTCHA_PRIVATE_KEY = '6LdRyD4pAAAAAAnFF2VVAn3QlDu0jlr2Ar-SJ8LJ'



CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'book_cache'),
    }
}

MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }

STRIPE_PUBLISHABLE_KEY = 'pk_test_51Ok22ACWrxSbdqrGdmUOQl1FknrVrNj9WsQM2E4K6uu4Q4uHb9MMNHld0Kyt0n4cdK7ZHHkNpGzKCKbSxcx4WGhm00NypnWe61'
STRIPE_SECRET_KEY = 'sk_test_51Ok22ACWrxSbdqrGS6ZuT98oQk9XX6h86YR5LdGHL0FXe725SFUPffcFGfNtlrXofjK6wjKJOwzzFr2HGPbQAnnS00B4d7lDpx'
STRIPE_API_VERSION = '2023-10-16'

STRIPE_WEBHOOK_SECRET = 'whsec_cd58edca6b6037c0897692cd7e7d256fbe73af66af64cd98616653a63d51d0a9'
