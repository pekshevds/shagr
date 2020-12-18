# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u0872810/data/www/shagr.ru/shagr')
sys.path.insert(1, '/var/www/u0872810/data/shagrenv/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'shagr.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()