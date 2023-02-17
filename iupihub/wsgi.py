"""
WSGI config for iupihub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application

path = []
path.append("/home/jasielrt95/iupihub")
path.append("/home/jasielrt95/iupihub/iupihub")
if path not in sys.path:
    sys.path.append(path)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iupihub.settings")

application = get_wsgi_application()
