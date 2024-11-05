from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class TextType(TextChoices):
    HELLO = "hello", _("Hello")
    BYE = "bye", _("Bye")


class LanguageChoice(TextChoices):
    UZ = "uz", "uz"
    RU = "ru", "ru"
    EN = "en", "en"