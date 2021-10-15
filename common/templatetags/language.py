from django.utils import translation
from django_jinja import library

from rpg_notes.settings import LANGUAGES


@library.global_function()
def language_code():
    return translation.get_language()


@library.global_function()
def all_languages():
    return LANGUAGES
