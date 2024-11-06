from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.agent.models import Agent
from apps.shared.tasks import get_changes, log_changes, action_log


class AgentUpdateSerializer(ModelSerializer):
    class Meta:
        model = Agent
        fields = (
            "id",
            "useranme",
            "first_name",
            "last_name",
            "email",
            "extensions",
            "phone",
            "avatar",
            "is_active",
            "not_ready_time",
            "user_permissions",
            "branch",
        )

    def validate_username(self, value):
        agent = self.context["request"].user
        if Agent.objects.exclude(pk=agent.pk).filter(username=value).exists():
            raise ValidationError({"username": "This username is already in use."})
        return value
    
    def update(self, instance, validated_data):
        request = self.context["request"]

        org_instance = Agent.objects.get(pk=instance.pk)
        
        changes = get_changes(org_instance, validated_data)
        instance = super().update(instance, validated_data)

        log_changes(instance, request, changes)

        return instance
