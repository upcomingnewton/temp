# Django settings for ThoughtXplore project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
	('nitin','upcomingnewton@gmail.com'),
	('sarvpriye','sarvpriye98@gmail.com'),
	('nitin','nitin@thoughtxplore.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'testdb',                      # Or path to database file if using sqlite3.
        'USER': 'test123',                      # Not used with sqlite3.
        'PASSWORD': 'test123db',                  # Not used with sqlite3.
        'HOST': '119.18.58.214',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'thoughtxplore@gmail.com'
EMAIL_HOST_PASSWORD = 'NewalaTX:)'
EMAIL_PORT = 587
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/home/nitin/Downloads/tx_latest/ThoughtXplore/ThoughtXplore/static',
     "/home/nitin/projects/temp/ThoughtXplore/static",
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '!wo!*jq0!lrkw5lr1*(#+$6a9zm(16sdo&zhvtj6pn*q$+j7u&'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'ThoughtXplore.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #"/home/nitin/Downloads/tx_latest/ThoughtXplore/ThoughtXplore/templates",
     "/home/nitin/projects/temp/ThoughtXplore/templates",
)

INSTALLED_APPS = (
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    #'django.contrib.sites',
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'txMisc',
    'txUser',
    'txCommunications',
    'txMenu',
    'UserContact',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    #'django.core.context_processors.i18n',
    #'django.core.context_processors.media',
    'django.core.context_processors.static',
    #'django.contrib.auth.context_processors.auth',
    #'django.contrib.messages.context_processors.messages',
    'ThoughtXplore.txContextProcessors.MenuContextProcessor',
    'ThoughtXplore.txContextProcessors.UserContextProcessor',
    'ThoughtXplore.txContextProcessors.TEMPLATE_PARAM_USER_NOT_LOGGED_IN',
    'ThoughtXplore.txContextProcessors.MessageContextProcessor',
    
)
# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = LOG_SETTINGS = {
    'version': 1,
    'loggers':{
               'LOGGER_UserSystem':{
                                    'handlers':['file_user','smtp'],
                                    'level':'DEBUG',
                                    },
               
                'LOGGER_MiscSystem':{
                                    'handlers':['file_misc','smtp'],
                                    'level':'DEBUG',
                                    },
               'LOGGER_QueryLogger':{
                                     'handlers':['file_query','smtp'],
                                    'level':'DEBUG',
                   },
               },
    'handlers': {
        'file_user': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/home/nitin/logs/tx_user_system',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'file_misc': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/home/nitin/logs/tx_misc_system',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
         'file_query': {
            'class': 'logging.handlers.RotatingFileHandler',
            'level': 'DEBUG',
            'formatter': 'detailed',
            'filename': '/home/nitin/logs/tx_queries',
            'maxBytes': 10485760,
            'backupCount': 5,
        },
        'smtp': {
            'class': 'logging.handlers.SMTPHandler',
            'level': 'ERROR',
            'formatter': 'email',
            'mailhost': 'localhost',
            'fromaddr': 'no-reply@thoughtxplore.com',
            'toaddrs': ['upcomingnewton@gmail.com', 'sarvpriye98@gmail.com'],
            'subject': '[ThoughtXplore] Error encountered.',
        },
    },
    'formatters': {
        'detailed': {
            'format': '%(asctime)s %(module)-17s line:%(lineno)-4d ' \
            '%(levelname)-8s %(message)s',
        },
        'email': {
            'format': 'Timestamp: %(asctime)s\nModule: %(module)s\n' \
            'Line: %(lineno)d\nMessage: %(message)s',
        },
    },
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'TIMEOUT':24*60*60,
    }
}
SESSION_ENGINE="django.contrib.sessions.backends.cached_db"
SESSION_COOKIE_AGE = 1*60
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
