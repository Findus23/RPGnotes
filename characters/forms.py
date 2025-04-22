from django.core.exceptions import ValidationError
from django.db import connection
from django.forms import ModelForm
from django.utils.text import slugify
from django.utils.translation import gettext as _

from characters.models import Character
from users.models import TenantUser


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "description_md", "aliases", "player", "faction", "location",
                  "archived", "color", "token_image", "large_image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].queryset = TenantUser.objects \
            .filter(tenants=connection.get_tenant()) \
            .exclude(pk__in=[1, 2])

    def clean_name(self):
        name = self.cleaned_data.get('name')
        slug = slugify(name)
        if Character.objects.filter(slug=slug).exists():
            raise ValidationError(_('A character with this name already exists.'))
        return name
