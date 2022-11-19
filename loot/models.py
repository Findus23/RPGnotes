from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from characters.models import Character
from common.models import DescriptionModel, HistoryModel, AliasModel
from locations.models import Location
from search.utils import NameSearchIndex
from utils.random_filename import get_file_path


class LootType(models.Model):
    name = models.CharField(_("Name"), max_length=1000)

    def __str__(self):
        return self.name


class Loot(DescriptionModel, AliasModel, HistoryModel):
    name = models.CharField(_("Name"), max_length=1000)
    quantity = models.PositiveSmallIntegerField(_("Quantity"))
    value_gold = models.DecimalField(_("Value (Gold)"), max_digits=7, decimal_places=2)
    weight = models.FloatField(_("Weight (lb)"), null=True, blank=True)
    image = ImageField(_("Image"), upload_to=get_file_path, blank=True, null=True)
    owner = models.ForeignKey(
        Character, on_delete=models.PROTECT,
        blank=True, null=True,
        verbose_name=_("Claimant"),
        related_name="loot"
    )
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT,
        blank=True, null=True,
        verbose_name=_("Location"),
        related_name="loot"
    )
    magic_item = models.BooleanField(_("Magic Item"), default=False)
    former = models.BooleanField(_("Former"), default=False)
    type = models.ForeignKey(
        LootType, on_delete=models.PROTECT,
        blank=True, null=True,
        verbose_name=_("Type"), related_name="loot"
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Loot")
        verbose_name_plural = _("Loot")
        indexes = [
            NameSearchIndex
        ]

    @property
    def value_per_unit(self):
        return self.value_gold / self.quantity

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('lootedit', args=[self.id])
