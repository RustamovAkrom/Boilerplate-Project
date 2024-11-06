from rest_framework.exceptions import ValidationError
from rest_framework.fields import DateTimeField, CharField
from rest_framework.serializers import ModelSerializer

from apps.agent.models import Agent
from apps.shared.tasks import get_changes, log_changes, action_log


class AgentRetriveUpdateDestroySerializer(ModelSerializer):
    date_joined = DateTimeField(read_only=True)
    last_login = DateTimeField(read_only=True)

    class Meta:
        model = Agent
        exclude = (
            "created_at",
            "updated_at",
            "user_permissions",
            "password",
        )
    
    def validate(self, attrs):
        request = self.context["request"]
        agent = request.user

        if agent.pk != self.instance.pk:
            raise ValidationError(
                {"authorize": "You don`t have permission for this Agent."}
            )
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        request = self.context["request"]

        org_instance = Agent.objects.get(pk=instance.pk)
        changes = get_changes(org_instance, validated_data)
        instance = super().update(instance, validated_data)
        log_changes(instance, request, changes)

        return instance


class ChangePasswordSerializer(ModelSerializer):
    password = CharField(write_only=True, required=True)
    password2 = CharField(write_only=True, required=True)
    old_password = CharField(write_only=True, required=True)

    class Meta:
        model = Agent
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        request = self.context["request"]
        agent = request.user
        instance = self.instance

        if attrs["password"] != attrs["password2"]:
            raise ValidationError({"password": "Password fields didn`n match."})
        
        if agent.role != "supervisor":
            if not agent.check_password(attrs["old_password"]):
                raise ValidationError("Old password is not correct.")

            if agent.pk != instance.pk:
                raise ValidationError(
                    {"authorize": "You do not have permission for this Agent."}
                )
        return attrs
    
    def update(self, instance, validated_data):
        request = self.context["request"]

        old_password = instance.password
        new_password = validated_data["password"]

        instance.set_password(new_password)
        instance.save()

        action_log(
            instance, 
            request, 
            "update", 
            "109", 
            old_value=old_password,
            new_value=new_password,
        )

        return instance
