""" 
Overrides settings.py (production) settings, for development. 

This file is imported only if the DJANGO_DEVELOPMENT environment variable is 
set to 'True'. You should set this variable in your virtualenv when working 
on the project.
"""

DEBUG = True

ALLOWED_HOSTS = ['localhost','127.0.0.1','192.168.1.77']

SECURE_SSL_REDIRECT = False
SESSION_COOKIE_SECURE = False
CSRF_COOKIE_SECURE = False
SECURE_HSTS_SECONDS = 0


