from django.contrib import admin
# Register your models here.
from simple_history.admin import SimpleHistoryAdmin

from notes.models import Character, Faction, Location, Loot, IngameDay, Session

admin.site.register(Character, SimpleHistoryAdmin)
admin.site.register(Faction, SimpleHistoryAdmin)
admin.site.register(Location, SimpleHistoryAdmin)
admin.site.register(Loot, SimpleHistoryAdmin)
admin.site.register(IngameDay, SimpleHistoryAdmin)
admin.site.register(Session, SimpleHistoryAdmin)
