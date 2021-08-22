from django.contrib import admin

# Register your models here.
from notes.models import Character, Campaign, Faction, Location, Loot

admin.site.register(Campaign)
admin.site.register(Character)
admin.site.register(Faction)
admin.site.register(Location)
admin.site.register(Loot)
