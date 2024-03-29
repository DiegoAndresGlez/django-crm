"""
WSGI config for dcrm project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

print(sys.path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcrm.settings')

application = get_wsgi_application()
