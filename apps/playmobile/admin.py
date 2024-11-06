from django.contrib import admin

from .models import Review, Text, BotLink


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("agent", "rating", "recipent")


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    pass


@admin.register(BotLink)
class BotLinkAdmin(admin.ModelAdmin):
    date_hierarchy = "updated_at"
    list_display = ("phone", "agent")
