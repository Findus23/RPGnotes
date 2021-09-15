from django.db import models
from simple_history.models import HistoricalRecords


class HistoryModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords(inherit=True)

    class Meta:
        abstract = True
