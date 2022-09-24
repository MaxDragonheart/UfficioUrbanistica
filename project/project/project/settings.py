"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 4.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import environ


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, [])
)
# reading .env file
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-g0e&_&b(3nale77)4^rve0!*mqw4i#=cc2q5o=72tn-!r$!6w)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'jazzmin',
    'tinymce',
    'bootstrap_italia_template',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.gis',
    'django.contrib.sites',
    'django.contrib.flatpages',

    'sections',
    'link',
    'media',
    'usermanager',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'link.context_processors.links_column1',
                'link.context_processors.links_column2',
                'link.context_processors.links_column3',
                'media.context_processors.highlighted_media',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PASSWORD'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'it'

TIME_ZONE = 'Europe/Rome'

USE_I18N = True

USE_TZ = True

DECIMAL_SEPARATOR = ','

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / '../static-folder'

MEDIA_URL = '/media/'
MEDIA_FOLDER = Path('../media-folder')
MEDIA_ROOT = BASE_DIR / MEDIA_FOLDER

STATICFILES_DIRS = [
        BASE_DIR / 'static',
    ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Corsheaders settings
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_METHODS = env('ALLOWED_HOSTS')
if not DEBUG:
    CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS')

# Django Tinymce
TINYMCE_DEFAULT_CONFIG = {
    "height": "800",
    "menubar": "file edit view insert format tools table help",
    "plugins": "advlist autolink lists link image charmap print preview anchor searchreplace visualblocks code "
                "fullscreen insertdatetime media table paste code help wordcount spellchecker",
    "toolbar": "undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft "
                "aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor "
                "backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | "
                "fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | "
                "a11ycheck ltr rtl | showcomments addcomment code",
    "custom_undo_redo_levels": 10,
}

# Usermanager App
AUTH_USER_MODEL = 'usermanager.UserProfile'
ADMIN_PANEL_ROOT = "area-riservata"
LOGIN_REDIRECT_URL = f"/{ADMIN_PANEL_ROOT}/"
LOGOUT_REDIRECT_URL = "/"

# Project settings
SITE_ID = 1
ADMIN_USERNAME = env('ADMIN_USERNAME')
ADMIN_PASSWORD = env('ADMIN_PASSWORD')
DOMAIN_NAME = env('DOMAIN_NAME')
DOMAIN = env('DOMAIN')
SITE_TITLE = env('SITE_TITLE')
SITE_LOGO = env('SITE_LOGO')
SITE_DESCRIPTION = env('SITE_DESCRIPTION')
ADDRESS = env('ADDRESS')
CONTACT_PHONE = env('CONTACT_PHONE')
CONTACT_EMAIL = env('CONTACT_EMAIL')
CONTACT_OFFICIAL_EMAIL = env('CONTACT_OFFICIAL_EMAIL')
