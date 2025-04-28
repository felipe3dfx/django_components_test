SECRET_KEY = 'test'  # noqa: S105

PASSWORD_HASHERS = ('django.contrib.auth.hashers.MD5PasswordHasher',)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
}

STORAGES = {
    'default': {
        'BACKEND': 'django.core.files.storage.FileSystemStorage',
    },
    'staticfiles': {
        'BACKEND': 'django.contrib.staticfiles.storage.StaticFilesStorage',
    },
}
