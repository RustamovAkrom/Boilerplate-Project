import os

CELERY_APP_NAME = "telemarketing"
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://127.0.0.1:6379")
CELERY_RESULT_BACKEND = "django-db"
CELERY_ACCEPT_CONTENT = ["application/json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE = "Asia/Tashkent"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60  # 30m
CELERY_CACHE_BACKEND = "default"
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"
CELERY_IMPORTS = (
    "apps.agent.tasks",
    "apps.cisco.tasks",
    "apps.playmobile.tasks",
)