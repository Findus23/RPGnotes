from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.text import slugify
from django.utils.translation import gettext as _

from loot.models import Loot


class LootForm(ModelForm):
    class Meta:
        model = Loot
        fields = ["name", "type", "aliases", "description_md", "quantity", "value_gold", "weight", "image",
                  "owner", "location", "magic_item", "former"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        pk = self.instance.pk if self.instance is not None else None
        slug = slugify(name)
        if Loot.objects.filter(slug=slug).exclude(pk=pk).exists():
            raise ValidationError(_('Loot with this name already exists.'))
        return name
