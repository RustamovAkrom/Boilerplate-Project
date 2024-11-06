from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.agent.models import Agent
from apps.shared.tasks import get_changes, log_changes, action_log


