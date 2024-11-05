from django.contrib.auth.models import Permission
from django.contrib import admin

from .models import (
    AgentSchedule,
    Agent,
    AgentGroup,
    AgentPosition,
    AgentInfo,
    CallLog,
)

@admin.register(AgentGroup)
class AgentGroupAdmin(admin.ModelAdmin):
    pass


@admin.register(AgentPosition)
class AgentPositionAdmin(admin.ModelAdmin):
    pass


@admin.register(AgentInfo)
class AgentInfoAdmin(admin.ModelAdmin):
    pass


@admin.register(AgentSchedule)
class AgentScheduleAdmin(admin.ModelAdmin):
    search_fields = ("phone", "date")
    list_display = ("phone", "shift", "sent", "date")


@admin.register(Agent)
class AgentAdmin(admin.ModelAdmin):
    list_display_links = ("username",)
    search_fields = ("phone", "username", "first_name", "last_name", "extension")
    list_display = ("phone", "username", "first_name", "last_name", "extension")


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "content_type", "codename")
    search_fields = ("name", "content_type")
    list_filter = ("content_type",)


@admin.register(CallLog)
class CallLogAdmin(admin.ModelAdmin):
    date_hierarchy = "created_at"
    list_filter = ("agent",)
    search_fields = ("fromAddress", "toAddress", "type")
