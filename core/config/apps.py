DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
CUSTOM_APPS = [
    "apps.shared.apps.SharedConfig",
    "apps.agent.apps.AgentConfig",
    "apps.calculator.apps.CalculatorConfig",
    "apps.cisco.apps.CiscoConfig",
    "apps.kpi.apps.KpiConfig",
    "apps.playmobile.apps.PlaymobileConfig",
    "apps.processing.apps.ProcessingConfig",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework_simplejwt",
    "django_celery_beat",
    "django_celery_results",
    "django_filters",
    "drf_yasg",
]