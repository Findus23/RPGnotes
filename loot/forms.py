from django.forms import ModelForm

from loot.models import Loot


class LootForm(ModelForm):
    class Meta:
        model = Loot
        fields = ["name", "description_md", "quantity", "value_gold", "owner", "location", "magic_item"]
