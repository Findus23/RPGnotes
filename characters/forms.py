from django.forms import ModelForm

from characters.models import Character


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "description_md", "subtitle", "player", "color", "image"]
