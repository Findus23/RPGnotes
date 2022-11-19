from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from loot.models import Loot, LootType

admin.site.register(Loot, SimpleHistoryAdmin)
admin.site.register(LootType)
