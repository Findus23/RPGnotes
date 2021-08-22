from django.conf import settings
from django.db import models
from simple_history.models import HistoricalRecords

from notes.models import Campaign, DescriptionModel


class Loot(DescriptionModel):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)

    name = models.CharField(max_length=1000)
    quantity = models.PositiveSmallIntegerField()
    value_gold = models.DecimalField("Value (Gold)", max_digits=7, decimal_places=2)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    magic_item = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    @property
    def value_per_unit(self):
        return self.value_gold / self.quantity

    def __str__(self):
        return self.name
