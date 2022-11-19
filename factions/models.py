from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from common.models import DescriptionModel, HistoryModel, NameSlugModel, AliasModel
from search.utils import NameSearchIndex


class Faction(NameSlugModel, DescriptionModel, AliasModel, HistoryModel):
    class Meta:
        ordering = ["name"]
        verbose_name = _("Faction")
        verbose_name_plural = _("Factions")
        indexes = [
            NameSearchIndex
        ]

    def get_absolute_url(self):
        return reverse('factiondetail', args=[self.slug])

    @property
    def graphkey(self):
        return f"fac{self.pk}"
