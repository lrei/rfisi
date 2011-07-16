import os
import sys

path = '/home/martinhelder'
path2 = '/home/martinhelder/rfisi'
if path not in sys.path:
    sys.path.append(path)
if path2 not in sys.path:
    sys.path.append(path2)


os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
