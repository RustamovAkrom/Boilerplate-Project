import logging

from .models import ActionModel, ActionDescription, FieldActionMapping


logger = logging.getLogger(__name__)


def action_log(
    instance, request, action, description_mode, new_value=None, old_value=None
):
    user_id = request.user.id
    ip_address = get_user_ip(request)
    description = ActionDescription.objects.filter(code=description_mode).first()

    write_action_log(
        action, user_id, description, instance, old_value, new_value, ip_address
    )


def write_action_log(
    action, 
    user_id, 
    description,
    instance,
    old_value=None,
    new_value=None,
    ip_address=None,
):
    ActionModel.objects.create(
        action_type=action,
        user_id=user_id,
        description=description,
        object_id=instance.id,
        old_value=old_value,
        new_value=new_value,
        ip_address=ip_address,
        history_for=instance,
    )


def get_changes(org_instance, validated_data, m2m_fields=None):
    changes = {}

    for field_name, new_value in validated_data.items():
        old_value = getattr(org_instance, field_name)
        if old_value != new_value:
            changes[field_name] = (old_value, new_value)
    
    if m2m_fields:
        for field_name in m2m_fields:
            old_value = list(getattr(org_instance, field_name).all())
            new_value = list(validated_data.pop(field_name, []))
            
            if old_value != new_value:
                changes[field_name] = (old_value, new_value)

    return changes


def log_changes(instance, request, changes):
    for field_name, (old_value, new_value) in changes.items():
        action_mapping = FieldActionMapping.objects.filter(
            field_name=field_name
        ).first()

        if action_mapping:
            action_log(
                instance=instance,
                request=request,
                action="update",
                description_mode=action_mapping.action_code,
                old_value=old_value,
                new_value=new_value,
            )


def get_user_ip(request):
    x_forwarded_for = None

    if request.META:
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip
