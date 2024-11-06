from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models


class ActionTypeChoice(models.TextChoices):
    CREATED = "create", _("Create")
    UPDATED = "update", _("Update")
    DELETED = "delete", _("Delete")


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugStampedModel(models.Model):
    slug = models.SlugField(unique=True)

    class Meta:
        abstract = True


class FieldActionMapping(TimeStampedModel):
    field_name = models.CharField(max_length=100, unique=True)
    action_code = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.field_name
    

class ActionModel(TimeStampedModel):
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    action_type = models.CharField(
        max_length=10, choices=ActionTypeChoice.choices, default=None
    )
    description = models.ForeignKey(
        "shared.ActionDescription", on_delete=models.SET_NULL, null=True, blank=True
    )
    content_type = models.ForeignKey(ContentType, on_delete=models.SET_NULL, null=True)
    object_id = models.PositiveBigIntegerField(null=True)
    history_for = GenericForeignKey("content_type", "object_id")
    user = models.ForeignKey(
        "agent.Agent", related_name="actions", on_delete=models.SET_NULL, null=True
    )
    ip_address = models.CharField(max_length=25)

    def __str__(self) -> str:
        return f"Histroy for {self.content_type} and {self.object_id}"
    

class ActionDescription(TimeStampedModel):
    description = models.TextField(null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True, unique=True)

    class Meta:
        verbose_name = _("ActionDescription")
        verbose_name_plural = _("ActionDescriptions")

    def __str__(self) -> str:
        return self.description
