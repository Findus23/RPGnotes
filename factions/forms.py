from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.utils.text import slugify
from django.utils.translation import gettext as _

from factions.models import Faction


class FactionForm(ModelForm):
    class Meta:
        model = Faction
        fields = ["name", "aliases", "description_md"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        slug = slugify(name)
        if Faction.objects.filter(slug=slug).exists():
            raise ValidationError(_('A faction with this name already exists.'))
        return name
