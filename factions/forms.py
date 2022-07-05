from django.forms import ModelForm

from factions.models import Faction


class FactionForm(ModelForm):
    class Meta:
        model = Faction
        fields = ["name", "aliases","description_md"]
