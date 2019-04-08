
from .base import *

DEBUG = 'FALSE'

ALLOWED_HOSTS = ['www.davidlevwilson.com']

with open('/home/DavidW/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

ADMINS = ('Webmaster', 'dave@davidlevwilson.com')
MANAGERS = ADMINS

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = False

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'dave@davidlevwilson.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


try:
    from .local import *
except ImportError:
    pass
