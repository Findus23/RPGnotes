from datetime import date

from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords


class Session(models.Model):
    day = models.DateField(default=date.today)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-day"]

    def get_absolute_url(self):
        return reverse('sessiondetail', args=[self.id])

    def __str__(self):
        return str(self.day)
