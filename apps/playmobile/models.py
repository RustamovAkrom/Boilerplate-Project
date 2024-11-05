from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from apps.shared.models import TimeStampedModel
from .choices import TextType, LanguageChoice


class Text(TimeStampedModel):
    body = models.TextField()
    type = models.CharField(max_length=6, choices=TextType.choices)
    due_interval = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.body


class Review(TimeStampedModel):
    agent = models.ForeignKey("agent.Agent", models.PROTECT, related_name="reviews")
    recipent = PhoneNumberField(region="UZ")
    text = models.ForeignKey("playmobile.Text", models.PROTECT, related_name="reviews")
    rating = models.IntegerField(default=-1)
    is_answared = models.BooleanField(default=False)
    appeal = models.ForeignKey("telemarketing.Appeal", models.PROTECT, related_name="reviews")
    language_code = models.CharField(
        max_length=2, choices=LanguageChoice.choices, default=LanguageChoice.EN
    )
    
    def __str__(self) -> str:
        return f" {self.recipent} - {self.agent} - {self.rating} "


class BotLink(TimeStampedModel):
    phone = PhoneNumberField(region="UZ")
    text = models.TextField(default="https://t.me/Asaka_bank_bot")
    agent = models.ForeignKey("agent.Agent", models.SET_NULL, related_name="links", null=True)

    def __str__(self) -> str:
        return f" {self.phone} - {self.text} - {self.agent} "
