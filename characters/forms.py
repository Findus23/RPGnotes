from django.db import connection
from django.forms import ModelForm

from characters.models import Character
from users.models import TenantUser


class CharacterForm(ModelForm):
    class Meta:
        model = Character
        fields = ["name", "description_md", "aliases", "subtitle", "player", "faction", "location",
                  "archived", "color", "token_image", "large_image"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['player'].queryset = TenantUser.objects \
            .filter(tenants=connection.get_tenant()) \
            .exclude(pk__in=[1, 2])
