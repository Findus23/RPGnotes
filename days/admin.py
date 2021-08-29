from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from days.models import IngameDay, Session

admin.site.register(IngameDay, SimpleHistoryAdmin)
admin.site.register(Session, SimpleHistoryAdmin)
