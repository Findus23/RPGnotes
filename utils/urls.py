from typing import Dict

from characters.models import Character
from locations.models import Location
from loot.models import Loot


def name2url() -> Dict[str, str]:
    data = {}

    for character in Character.objects.all():
        data[character.firstname] = character.get_absolute_url()
    for location in Location.objects.all():
        data[location.name] = location.get_absolute_url()
    for loot in Loot.objects.all():
        data[loot.name] = loot.get_absolute_url()
    return data
