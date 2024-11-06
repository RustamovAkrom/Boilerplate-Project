from django.contrib.contenttypes.models import ContentType

from rest_framework import serializers

from apps.agent.models import Agent
from .models import ActionModel, ActionDescription


class ContentTypeMixin(serializers.Serializer):
    content_type = serializers.SerializerMethodField()

    def get_content_type(self, obj):
        return ContentType.objects.get_for_model(obj).id
    

class UserSerializerForActionLog(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "is_active",
            "role",
            "email",
            "extension",
        )


class ActionDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionDescription
        fields = ("id", "description", "code", )


class ActionModelSerializer(serializers.ModelSerializer):
    user = UserSerializerForActionLog(read_only=True)
    description = ActionDescriptionSerializer(read_only=True)

    class Meta:
        model = ActionModel
        fields = (
            "id",
            "user",
            "action_type",
            "created_at",
            "content_type",
            "description",
            "ip_address",
            "new_value",
            "object_id",
            "old_value",
        )