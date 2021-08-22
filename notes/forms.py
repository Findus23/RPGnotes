from django.forms import ModelForm

from notes.models import Campaign, Loot, Character


class CampaignForm(ModelForm):
    class Meta:
        model = Campaign
        fields = "__all__"


class LootForm(ModelForm):
    class Meta:
        model = Loot
        fields = ["name", "description_md", "quantity", "value_gold", "owner", "magic_item"]


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "description_md", "subtitle", "player", "faction", "location", "color", "image"]
