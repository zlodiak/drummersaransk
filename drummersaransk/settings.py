import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = '-a#&=-0i$_6$g0jfsvztxe*s#qp75dvvvfgzxqpv2&=u2-zny2'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'drummersaransk',
    #'sitetree',
    'debug_toolbar',
    'captcha',
    'sorl.thumbnail',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'drummersaransk.urls'

WSGI_APPLICATION = 'drummersaransk.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

TIME_ZONE = 'Europe/Moscow'

LANGUAGE_CODE = 'ru-ru'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATIC_URL = '/static/'

STATICFILES_DIRS = (
	(os.path.join(BASE_DIR, "drummersaransk/static/")),

)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


TEMPLATE_DIRS = (
	os.path.join(BASE_DIR, 'drummersaransk/templates/'),
	os.path.join(BASE_DIR, 'drummersaransk/templates/accounts/'),
	os.path.join(BASE_DIR, 'drummersaransk/templates/userprofile/'),
	os.path.join(BASE_DIR, 'drummersaransk/templates/user/'),
	os.path.join(BASE_DIR, 'drummersaransk/templates/right_col/'),
	os.path.join(BASE_DIR, 'drummersaransk/templates/userprofile/path_glory/'),

)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
)


ALLOWED_HOSTS = ['127.0.0.1:8000']

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            #'filename': 'C:/Python33/django_projects/mutants/debug.log',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}


THUMBNAIL_DEBUG = False



