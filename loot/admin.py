from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from loot.models import Loot

admin.site.register(Loot, SimpleHistoryAdmin)
