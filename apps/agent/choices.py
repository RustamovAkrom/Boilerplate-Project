from django.utils.translation import gettext_lazy as _
from django.db import models


class AgentRoleChoice(models.TextChoices):
    AGENT = "agent", _("Agent")
    MANAGER = "manager", _("Manager")
    ADMIN = "admin", _("Admin")
    SUPERVISOR = "supervisor", _("Supervisor")
    BRANCH = "branch", _("Branch")
