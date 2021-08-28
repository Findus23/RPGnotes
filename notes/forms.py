from django.forms import ModelForm, ModelMultipleChoiceField, CheckboxSelectMultiple

from notes.models import  Loot, Character, IngameDay, Session



class LootForm(ModelForm):
    class Meta:
        model = Loot
        fields = ["name", "description_md", "quantity", "value_gold", "owner", "magic_item"]


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "description_md", "subtitle", "player", "faction", "location", "color", "image"]


class DayForm(ModelForm):
    sessions = ModelMultipleChoiceField(
        queryset=Session.objects.all(),
        widget=CheckboxSelectMultiple()
    )

    class Meta:
        model = IngameDay
        fields = ["day", "description_md", "sessions"]
