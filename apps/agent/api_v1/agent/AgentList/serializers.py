from rest_framework.serializers import ModelSerializer
from apps.agent.models import Agent
from apps.shared.serializers import ContentTypeMixin


class AgentListSerializer(ContentTypeMixin, ModelSerializer):
    class Meta:
        model = Agent
        fields = (
            "id",
            "last_login",
            "is_superuser",
            "username",
            "first_name",
            "last_name",
            "is_staff",
            "is_active",
            "date_joined",
            "phone",
            "role",
            "email",
            "avatar",
            "extension",
            "content_type",
            "branch",
        )
