from modeltranslation.translator import translator, TranslationOptions

from .models import (
    Credit, 
    Type, 
    CustomerStatus, 
    CustomerCategory,
    AppealStatus, 
    Product, 
    ScriptCategory, 
    Script, Option, 
    CallScript,
)


class CreditTranslationOptions(TranslationOptions):
    fields = ("name", )


class TypeTranslationOptions(TranslationOptions):
    fields = ("name", )


class CustomerStatusTranslationOptions(TranslationOptions):
    fields = ("name", )


class CustomerCategoryTranslationOptions(TranslationOptions):
    fields = ("name", )


class AppealStatusTranslationOptions(TranslationOptions):
    fields = ("name", )


class ProductTranslationOptions(TranslationOptions):
    fields = ("name", "info", )


class ScriptCategoryTranslationOptions(TranslationOptions):
    fields = ("name", )


class ScriptTranslationOptions(TranslationOptions):
    fields = ("title", )


class OptionTranslationOptions(TranslationOptions):
    fields = ("name", )


class CallScriptTranslationOptions(TranslationOptions):
    fields = ("text", )


translator.register(Credit, CreditTranslationOptions)
translator.register(Type, TypeTranslationOptions)
translator.register(CustomerStatus, CustomerStatusTranslationOptions)
translator.register(CustomerCategory, CustomerCategoryTranslationOptions)
translator.register(AppealStatus, AppealStatusTranslationOptions)
translator.register(Product, ProductTranslationOptions)
translator.register(ScriptCategory, ScriptCategoryTranslationOptions)
translator.register(Script, ScriptTranslationOptions)
translator.register(Option, OptionTranslationOptions)
translator.register(CallScript, CallScriptTranslationOptions)
