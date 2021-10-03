from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from factions.models import Faction

admin.site.register(Faction, SimpleHistoryAdmin)
