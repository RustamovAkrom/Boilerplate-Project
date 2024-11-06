from django_filters import rest_framework as filters

from apps.agent.models import Agent


class AgentFilter(filters.FilterSet):
    class Meta:
        model = Agent
        fields = ("role", "position", "group")
