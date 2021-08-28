from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

from notes.models import Session, DescriptionModel


class IngameDay(DescriptionModel):
    day = models.PositiveIntegerField()
    sessions = models.ManyToManyField(Session, related_name="ingame_days")

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-day"]

    def get_absolute_url(self):
        return reverse('daydetail', args=[self.day])

    @property
    def prettyname(self):
        return ordinal(self.day) + " day"

    def __str__(self):
        return self.prettyname
