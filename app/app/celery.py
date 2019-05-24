from __future__ import absolute_import
import os
from celery import Celery

from app import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app', broker='redis://localhost:6379')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# celery -A app.celery worker -l DEBUG -E