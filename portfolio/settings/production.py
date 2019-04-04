
from .base import *

DEBUG = 'FALSE'

ALLOWED_HOSTS = ['www.davidlevwilson.com']

with open('/home/DavidW/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

ADMINS = ('Webmaster', 'dave@davidlevwilson.com')
MANAGERS = ADMINS

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'dave@davidlevwilson.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'Fresh1973$$$'

try:
    from .local import *
except ImportError:
    pass
