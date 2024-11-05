from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import TimeStampedModel


class SendMyId(TimeStampedModel):
    agent = models.ForeignKey("agent.Agent", models.PROTECT)
    phone = PhoneNumberField(region="UZ")
    lang = models.CharField(max_length=2)
    