from django.forms import ModelForm

from loot.models import Loot


class LootForm(ModelForm):
    class Meta:
        model = Loot
        fields = ["name", "aliases", "description_md", "quantity", "value_gold", "weight", "image", "owner", "location",
                  "magic_item"]
