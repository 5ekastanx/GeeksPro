from pathlib import Path
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-@$ez1@qgt-aaz6_zjv$%mpeegcw44zsfn&yqhhv$w&^26^e6ko'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'apps.trainees',
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

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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

# Полный список всех поддерживаемых языков проекта
ALL_PROJECT_LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
    ('en', _('English')),
]

# По умолчанию (до применения middleware) активны все
LANGUAGES = ALL_PROJECT_LANGUAGES

MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'
# Это важно: чтобы modeltranslation не падал, если язык отключен
MODELTRANSLATION_FALLBACK_LANGUAGES = ('ru', 'ky', 'en')

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"

STATICFILES_DIRS = [
    BASE_DIR / "static",
]


JAZZMIN_SETTINGS = {
    # Название вкладки браузера (title страницы)
    "site_title": "Администрация стажеров",

    # Большой заголовок сверху в админ панели
    "site_header": "Управление стажерами",

    # Текст рядом с логотипом в левом верхнем углу
    "site_brand": "Группа стажеров",

    # Приветственный текст на главной странице админки
    "welcome_sign": "Добро пожаловать в панель управления стажерами!",

    # Текст внизу админ панели (footer)
    "copyright": "Бекастан",

    # Логотип
    "site_logo": "/img/logo.png",
    "login_logo": "/img/logo.png",
    "site_logo_classes": "img-circle",

    # Поиск по моделям (можно указать модели, по которым будет работать поиск в админке)
    "search_model": ["auth.User"],

    # Сортировка приложений
    "order_with_respect_to": [
        "trainees",
        "auth",
        "auth.user",
        "auth.group",
    ],

    # Иконки
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        "trainees": "fas fa-user-graduate",
        "trainees.trainee": "fas fa-id-card",
    },

    # Верхнее меню
    "topmenu_links": [
        {"name": "Home", "url": "admin:index"},
        {"model": "auth.User"},
        {"app": "trainees"},
    ],

    "related_modal_active": False,

    # UI builder (можно менять тему)
    "show_ui_builder": False,
}


JAZZMIN_UI_TWEAKS = {
    # Основная тема админки (светлая, классическая)
    "theme": "flatly",

    # Цвет верхней панели навигации (navbar)
    "navbar": "navbar-light",

    # Цвет бокового меню (sidebar)
    "sidebar": "sidebar-light-primary",

    # Цвет бренда (текст рядом с логотипом)
    "brand_colour": "navbar-light",

    # Акцентный цвет (кнопки, ссылки и активные элементы)
    "accent": "accent-primary",

    # Фиксированная верхняя панель (при скролле страницы остаётся видимой)
    "navbar_fixed": True,

    # Фиксированная боковая панель (при скролле остаётся видимой)
    "sidebar_fixed": True,
}
