from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Keamanan dasar
SECRET_KEY = 'django-insecure-(=f^g6v0_e)3d-%t=i#$xb=r+hxp@^7y-623(g463%%!!jo(kv'
DEBUG = True
ALLOWED_HOSTS = []

# Aplikasi yang digunakan
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'news',
    'ckeditor',
    'ckeditor_uploader',
    'dj_database_url',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'senblog.urls'

# Template config
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'senblog.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validasi Password
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

# Bahasa dan waktu
LANGUAGE_CODE = 'id'  # ← disesuaikan ke bahasa Indonesia
TIME_ZONE = 'Asia/Jakarta'  # ← waktu lokal Indonesia

USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static dan Media
STATIC_URL = 'static/'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# CKEditor Upload
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 300,
        'width': 'auto',
    },
}

# Primary key default
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
import dj_database_url

# Tambahkan ini di paling bawah settings.py:
if not DEBUG:
    ALLOWED_HOSTS = ['*']  # atau isi dengan domain Render nantinya
    DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)
    STATIC_ROOT = BASE_DIR / 'staticfiles'

import os
import dj_database_url

# Untuk production (Render)
if os.environ.get('RENDER'):
    DEBUG = False
    ALLOWED_HOSTS = ['firja-Project-UAS.onrender.com']  # Ganti nanti

    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600,
        )
    }

    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
