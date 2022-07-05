from typing import Dict

from characters.models import Character
from factions.models import Faction
from locations.models import Location
from loot.models import Loot
from notes.models import Note


def name2url() -> Dict[str, str]:
    data = {}
    objects=[]
    objects.extend(Character.objects.all())
    objects.extend(Location.objects.all())
    objects.extend(Loot.objects.all())
    objects.extend(Faction.objects.all())
    objects.extend(Note.objects.all())
    for object in objects:
        data[object.name] = object.get_absolute_url()
        if object.aliases:
            for alias in object.aliases:
                data[alias] = object.get_absolute_url()

    # longer replacements first
    data = {k: v for k, v in sorted(data.items(), key=lambda item: -len(item[0]))}
    return data
