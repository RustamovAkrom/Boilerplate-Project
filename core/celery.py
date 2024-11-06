import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core", broker=settings.CELERY_BROKER_URL)

app.config_from_object("core.settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
