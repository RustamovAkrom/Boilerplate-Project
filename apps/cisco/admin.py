from django.contrib import admin

from .models import ResourceStats


@admin.register(ResourceStats)
class ResourcesStatsAdmin(admin.ModelAdmin):
    list_filter = ("resourceName", )