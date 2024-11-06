from modeltranslation.translator import translator, TranslationOptions
from .models import ActionDescription


class ActionDescriptionTranslationOptions(TranslationOptions):
    fields = (
        "description",
    )


translator.register(ActionDescription, ActionDescriptionTranslationOptions)
