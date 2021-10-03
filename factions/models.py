from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from common.models import DescriptionModel, HistoryModel, NameSlugModel


class Faction(NameSlugModel, DescriptionModel, HistoryModel):

    class Meta:
        ordering = ["name"]
        verbose_name = _("Faction")
        verbose_name_plural = _("Factions")

    def get_absolute_url(self):
        return reverse('factiondetail', args=[self.slug])

