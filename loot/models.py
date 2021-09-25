from django.db import models
from django.utils.translation import gettext_lazy as _

from characters.models import Character
from common.models import DescriptionModel, HistoryModel
from locations.models import Location


class Loot(DescriptionModel, HistoryModel):
    name = models.CharField(_("Name"), max_length=1000)
    quantity = models.PositiveSmallIntegerField(_("Quantity"))
    value_gold = models.DecimalField(_("Value (Gold)"), max_digits=7, decimal_places=2)
    weight = models.FloatField(_("Weight (lb)"), null=True, blank=True)
    owner = models.ForeignKey(Character, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("Claimant"))
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True, verbose_name=_("Location"))
    magic_item = models.BooleanField(_("Magic Item"), default=False)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Loot")
        verbose_name_plural = _("Loot")

    @property
    def value_per_unit(self):
        return self.value_gold / self.quantity

    def __str__(self):
        return self.name
