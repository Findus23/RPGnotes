from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

from common.models import DescriptionModel, HistoryModel


class Session(HistoryModel, models.Model):
    day = models.DateField(default=date.today)

    class Meta:
        ordering = ["-day"]

    def get_absolute_url(self):
        return reverse('sessiondetail', args=[self.id])

    def __str__(self):
        return str(self.day)


class IngameDay(DescriptionModel, HistoryModel):
    day = models.PositiveIntegerField()
    sessions = models.ManyToManyField(Session, related_name="ingame_days")

    class Meta:
        ordering = ["-day"]

    def get_absolute_url(self):
        return reverse('daydetail', args=[self.day])

    @property
    def prettyname(self):
        return ordinal(self.day) + " day"

    def __str__(self):
        return self.prettyname
