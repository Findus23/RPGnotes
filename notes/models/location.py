from django.db import models
from simple_history.models import HistoricalRecords

from notes.models import BaseModel, DescriptionModel


class Location(BaseModel, DescriptionModel):
    notes = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()
