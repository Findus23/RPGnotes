from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from characters.models import Character

admin.site.register(Character, SimpleHistoryAdmin)
