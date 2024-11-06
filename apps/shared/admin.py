from django.contrib.admin.models import LogEntry, DELETION
from django.http import HttpRequest
from django.utils.safestring import mark_safe
from django.utils.html import escape
from django.contrib import admin
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType

from .models import ActionModel, ActionDescription, FieldActionMapping


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    date_hierarchy = "action_time"

    list_filter = ("user", "content_type", "action_flag", )

    search_fields = (
        "object_repr",
        "change_message",
        "user__username",
    )

    list_display = (
        "action_time",
        "user",
        "content_type",
        "object_link",
        "action_flag",
    )

    def has_add_permission(self, request: HttpRequest) -> bool:
        return False
    
    def has_change_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    def has_delete_permission(self, request: HttpRequest, obj=None) -> bool:
        return False
    
    def has_view_permission(self, request: HttpRequest, obj=None) -> bool:
        return request.user.is_superuser
    
    def object_link(self, obj):
        if obj.action_flag == DELETION:
            link = escape(obj.object_repr)
        else:
            ct = obj.content_type
            link = '<a href="%s">%s</a>' % (
                reverse(
                    "admin:%s_%s_change" % (ct.app_label, ct.model),
                    args=[obj.object_id],
                ),
                escape(obj.object_repr)
            )
        return mark_safe(link)
    object_link.admin_order_field = "object_repr"
    object_link.short_description = "object"


@admin.register(ActionModel)
class ActionModelAdmin(admin.ModelAdmin):
    list_display = (
        "action_type",
        "user",
        "created_at",
        "description",
        "new_value",
        "old_value",
        "ip_address",
        "history_for",
    )
    search_fields = ("new_value", "old_value", "description")
    readonly_fields = (
        "created_at",
        "user",
        "updated_at",
        "old_value",
        "new_value",
        "history_for",
        "ip_address",
        "action_type",
        "description",
        "object_id",
        "content_type",
    )


@admin.register(ActionDescription)
class ActionDescriptionAdmin(admin.ModelAdmin):
    pass


@admin.register(FieldActionMapping)
class FieldActionMappingAdmin(admin.ModelAdmin):
    list_display = ("field_name", "action_code", "created_at", "updated_at")
    search_fields = ("field_name", "action_code")
    readonly_fields = ("created_at", "updated_at")


@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "app_label", "model")
    search_fields = ("app_label", "model")
