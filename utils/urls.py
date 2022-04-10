from typing import Dict

from characters.models import Character
from factions.models import Faction
from locations.models import Location
from loot.models import Loot
from notes.models import Note


def name2url() -> Dict[str, str]:
    data = {}

    for character in Character.objects.all():
        data[character.firstname] = character.get_absolute_url()
    for location in Location.objects.all():
        data[location.name] = location.get_absolute_url()
    for loot in Loot.objects.all():
        data[loot.name] = loot.get_absolute_url()
    for faction in Faction.objects.all():
        data[faction.name] = faction.get_absolute_url()
    for note in Note.objects.all():
        data[note.name] = note.get_absolute_url()

    # longer replacements first
    data = {k: v for k, v in sorted(data.items(), key=lambda item: -len(item[0]))}
    return data
