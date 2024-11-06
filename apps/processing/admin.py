from django.contrib import admin

from .models import UzcardHistroyRequest, HumoCardHistoryRequest, MasterCardHistoryRequest


@admin.register(UzcardHistroyRequest)
class UzcardHistoryRequestAdmin(admin.ModelAdmin):
    list_display = ("card_id", "created_at")


@admin.register(HumoCardHistoryRequest)
class HumoCardHistoryRequestAdmin(admin.ModelAdmin):
    list_display = ("card_number", "created_at")


@admin.register(MasterCardHistoryRequest)
class MasterCardHistoryRequestAdmin(admin.ModelAdmin):
    list_display = ("card_number", "created_at")
