from django.utils.translation import gettext_lazy as _
from django.db.models import TextChoices


class CallScriptChoice(TextChoices):
    HELLO = "hello", "hello"
    APPEAL = "appeal", "appeal"
    CONSULTATION = "consultation", "consultation"
    STATEMENT = "statement", "statement"
    CLIENT = "client", "client"
    BYE = "bye", "bye"


class CallScriptModuleChoice(TextChoices):
    TELEMARKETING = "telemarketing", "telemarketing"
    CONTACT_CENTER = "contact_center", "contact_center"


class CallStatus(TextChoices):
    INTERESTED = "interested", _("Interested")
    NOT_INTERESTED = "not_interested", _("Not Interested")
    DO_NOT_DISTRUB = "do_not_distrub", _("Do Not Distrub")
    CALLBACK = "callback", _("Callback")
    INFORMATION_LEFT = "information_left", _("Information Left")


class CustomerLevel(TextChoices):
    LOW = "low", _("Low")
    MEDIUM = "medium", _("Medium")
    HIGH = "high", _("High")


class ProductTypeChoice(TextChoices):
    HELLO = "calculator", "calculator"
    APPEAL = "chouse", "chouse"
    TEXT = "text", "text"
