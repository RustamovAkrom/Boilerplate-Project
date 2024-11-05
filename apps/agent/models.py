from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import TimeStampedModel
from .choices import AgentRoleChoice


class AgentGroup(TimeStampedModel):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    phone_number = PhoneNumberField(region="UZ", null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-id']


class AgentPosition(TimeStampedModel):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['-id']


class Agent(TimeStampedModel, AbstractUser):
    phone = PhoneNumberField(region="UZ", null=True, blank=True)
    role = models.CharField(
        max_length=10, choices=AgentRoleChoice, default=AgentRoleChoice.AGENT
    )
    email = models.EmailField(blank=True)
    avatar = models.ImageField(upload_to="agent/avatar/%Y/%m/%d", default="avatar.jpg")
    not_ready_time = models.BigIntegerField(default=0)
    extension = models.CharField(max_length=4, unique=True, null=True, blank=True)
    middle_name = models.CharField(max_length=150, blank=True, null=True)
    group = models.ForeignKey(AgentGroup, on_delete=models.SET_NULL, null=True)
    position = models.ForeignKey(AgentPosition, on_delete=models.SET_NULL, null=True)
    branch = models.ForeignKey(
        "telemarketing.Branch", models.SET_NULL, related_name="agents", null=True
    )

    class Meta:
        ordering = ['-id']


class AgentInfo(TimeStampedModel):
    user = models.OneToOneField(Agent, on_delete=models.CASCADE, related_name="info")
    pinfl = models.CharField(max_length=50, blank=True, null=True, unique=True)
    inn = models.CharField(max_length=50, blank=True, null=True)
    contract_number = models.CharField(max_length=100, blank=True, null=True)
    contract_date = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    date_of_berth = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return self.user.first_name
    
    class Meta:
        ordering = ['-id']


class AgentSchedule(TimeStampedModel):
    phone = PhoneNumberField(region="UZ")
    date = models.DateField()
    shift = models.IntegerField(validators=[MaxValueValidator(6), MinValueValidator(0)])
    sent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.phone} - {self.shift}"
    

class CallLog(TimeStampedModel):
    agent = models.ForeignKey("agent.Agent", on_delete=models.PROTECT, related_name="calls")
    fromAddress = models.CharField(max_length=28)
    toAddress = models.CharField(max_length=28)
    type = models.CharField(max_length=28)
    start_date = models.DateTimeField()
    end_data = models.DateTimeField()
    fill_from_time = models.IntegerField(default=0)

    class Meta:
        verbose_name = _("CallLog")
        verbose_name_plural = _("CallLogs")
