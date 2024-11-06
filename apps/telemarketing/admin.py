from django.contrib import admin

from .models import (
    Credit,
    Type,
    CustomerCategory,
    Customer,
    Appeal,
    AppealStatus,
    Comment,
    Chouse,
    Product,
    Channel,
    ScriptCategory,
    Script,
    OptionObject,
    Option,
    CallScript,
    Branch,
    Process
)

@admin.register(Credit)
class CreditAdmin(admin.ModelAdmin):
    pass


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomerCategory)
class CustomerCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(AppealStatus)
class AppealStatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "parent_id", )

    def parent_id(self, obj):
        return obj.parent.id  if obj.parent else None
    
    parent_id.short_description = "Parent Id"


@admin.register(ScriptCategory)
class ScriptCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Script)
class ScriptAdmin(admin.ModelAdmin):
    pass


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    pass


@admin.register(CallScript)
class CallScriptAdmin(admin.ModelAdmin):
    pass


admin.site.register(
    [Customer, Appeal, Channel, Chouse, Comment, OptionObject, Branch, Process]
)
