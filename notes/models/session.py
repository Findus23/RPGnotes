from datetime import date

from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

from notes.models import Campaign


class Session(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)

    day = models.DateField(default=date.today)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["-day"]
        unique_together = ["campaign", "day"]

    def get_absolute_url(self):
        return reverse('sessiondetail', args=[self.campaign.slug, self.id])

    def __str__(self):
        return str(self.day)
