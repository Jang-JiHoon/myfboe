from .base import *  # noqa
from .base import env

# GENERAL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = True
# https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = env(
    "DJANGO_SECRET_KEY",
    default="esgTtwvsGRcaJ6vwbtFGTtpbqPIu610xoWnpeT4kvAGXQOOAU1LTU3hpUcX7x2X0",
)
# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["localhost", "0.0.0.0", "127.0.0.1","112.221.126.141"]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# EMAIL
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = env(
    "DJANGO_EMAIL_BACKEND",
    default="django.core.mail.backends.smtp.EmailBackend",
    # EMAIL_HOST = 'smtp.gmail.com',
    # EMAIL_HOST_USER = 'wlgns1881@gmail.com',
    # EMAIL_HOST_PASSWORD = 'guswn3484@',
    # EMAIL_PORT = 587,
    # EMAIL_USE_TLS = True,
    # DEFAULT_FROM_EMAIL = 'wlgns1881@gmail.com',
    
)

# django-debug-toolbar
# ------------------------------------------------------------------------------
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#prerequisites
INSTALLED_APPS += ["debug_toolbar"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#middleware
MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware"]  # noqa F405
# https://django-debug-toolbar.readthedocs.io/en/latest/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    "DISABLE_PANELS": ["debug_toolbar.panels.redirects.RedirectsPanel"],
    "SHOW_TEMPLATE_CONTEXT": True,
}
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html#internal-ips
INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]


# django-extensions
# ------------------------------------------------------------------------------
# https://django-extensions.readthedocs.io/en/latest/installation_instructions.html#configuration
INSTALLED_APPS += ["django_extensions"]  # noqa F405

# Your stuff...
# ------------------------------------------------------------------------------
import socket
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_IP = socket.gethostbyname(EMAIL_HOST)
EMAIL_HOST_USER = 'ulsan@fboeit.com'
EMAIL_HOST_PASSWORD = 'fboe0719!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# GMAIL_API_CLIENT_ID  =  'fboe@fboeit.com' 
# GMAIL_API_CLIENT_SECRET  =  'fboe0719!' 
# GMAIL_API_REFRESH_TOKEN  =  'refresh_token'