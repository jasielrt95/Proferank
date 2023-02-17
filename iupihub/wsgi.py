import os
import sys

from django.core.wsgi import get_wsgi_application

path = ["/home/jasielrt95/iupihub", "/home/jasielrt95/iupihub/iupihub"]
sys.path.extend(path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iupihub.settings.production")

application = get_wsgi_application()
