import os

from django.conf import settings

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core", broker=settings.CELERY_BROKER_URL)

app.config_from_object("core.settings", namespace="CELERY")


app.conf.beat_schedule = {
    "send-sms-every-day-at-18": {
        "task": "apps.agent.tasks.send_sms_to_agents",
        "schedule": crontab(minute=0, hour=18),
    },
    "update-agent-not-ready-time-at-24": {
        "task": "apps.agent.tasks.update_not_read_time",
        "schedule": crontab(minute=0, hour=0),
    },
    # "save-daily-statistics": {
    #     "task": "apps.cisco.tasks.load_daily_resource",
    #     "schedule": crontab(minute=0, hour=18),
    # },
    # */5 * * * *
    # "debug-task": {
    #     "task": "apps.cisco.tasks.send_mail",
    #     "schedule": 10.0,
    # }
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
