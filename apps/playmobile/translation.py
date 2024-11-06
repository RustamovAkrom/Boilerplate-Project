from modeltranslation.translator import translator, TranslationOptions
from .models import Text


class TextTranslationOptions(TranslationOptions):
    fields = (
        "body",
    )

translator.register(Text, TranslationOptions)
