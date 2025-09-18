import os
from pathlib import Path

# Diretório base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Chave secreta e debug
SECRET_KEY = os.environ.get('SECRET_KEY', 'murubijr')
DEBUG = False  # Em produção, deve ser False
ALLOWED_HOSTS = ["goatelas-pdf-translator.onrender.com"]

# Apps instalados
INSTALLED_APPS = [
    'django.contrib.staticfiles',  # Essencial para servir estáticos
    'pdf',  # Sua app principal
]

# Middlewares
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # WhiteNoise para servir estáticos
    'django.middleware.common.CommonMiddleware',
]

# URLs principais
ROOT_URLCONF = 'tradutorpdf.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
            ],
        },
    },
]

# WSGI
WSGI_APPLICATION = 'tradutorpdf.wsgi.application'

# Idioma e fuso horário
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'Africa/Maputo'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Arquivos estáticos
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / "static"]  # Onde você mantém CSS/JS
STATIC_ROOT = BASE_DIR / "staticfiles"    # Onde collectstatic vai colocar
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Arquivos de mídia
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
