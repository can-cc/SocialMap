"""
Django settings for DjangoSocialMap project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'm_3llp#^-qsl3z#1moqho&e7_=z#1&zx(fwkqr(eeerm(k1ivt'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = '/socialMap/'
LOGOUT_REDIRECT_URL = '/socialMap/'
#CORS


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'SMGIS',
    'userManager',
    'userTrack',
    'markPost',
    'BasicServices',
    'corsheaders',
    'friends',
    #'middleware',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsPostCsrfMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'middleware.crossdomainxhr.XsSharing',
)


# XS_SHARING_ALLOWED_ORIGINS = 'http://192.168.199.188:9000'
#
# XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

ROOT_URLCONF = 'DjangoSocialMap.urls'

WSGI_APPLICATION = 'DjangoSocialMap.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    # 'default': {
    #      'ENGINE': 'django.contrib.gis.db.backends.mysql',
    #      'NAME': 'socialMap',
    #      'USER': 'root',
    #      'PASSWORD': 'tyanmysql',
    #      'HOST': 'localhost',
    #      'PORT': '3306',
    #  },
    # 'default': {
    #     'ENGINE': 'django.contrib.gis.db.backends.spatialite',
    #     'NAME': 'test.db'
    # }
    'default': {
         'ENGINE': 'django.contrib.gis.db.backends.postgis',
         'NAME': 'socialMap',
         'USER': 'tyan',
         'PASSWORD': 'tyanpost',
         # 'HOST': 'localhost',
         # 'PORT': '3306',
    },
}
# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = '../static/'
MEDIA_ROOT = '../media/'
MEDIA_URL = '/media/'

