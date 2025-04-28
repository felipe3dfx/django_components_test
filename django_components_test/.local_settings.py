import socket

DEBUG = True

if DEBUG:
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = ['127.0.0.1'] + ['.'.join(ip.split('.')[:-1] + ['1']) for ip in ips]
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'


ALLOWED_HOSTS: list = []

SECRET_KEY = ''


REDIS_HOST = 'redis'
REDIS_PORT = 6379

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/1',
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection._HiredisParser',
        },
    },
    'sessions': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}/2',
        'OPTIONS': {
            'PARSER_CLASS': 'redis.connection._HiredisParser',
        },
    },
}
