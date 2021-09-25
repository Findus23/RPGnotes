from datetime import date

from django.contrib.humanize.templatetags.humanize import ordinal
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from common.models import DescriptionModel, HistoryModel


class Session(HistoryModel, models.Model):
    date = models.DateField(_("Date"), default=date.today)

    class Meta:
        ordering = ["-date"]
        verbose_name = _("Session")
        verbose_name_plural = _("Sessions")

    def get_absolute_url(self):
        return reverse('sessiondetail', args=[self.id])

    def __str__(self):
        return str(self.date)


class IngameDay(DescriptionModel, HistoryModel):
    day = models.PositiveIntegerField(_("Day"))
    sessions = models.ManyToManyField(Session, related_name="ingame_days", verbose_name=_("Session"))

    class Meta:
        ordering = ["-day"]
        verbose_name = _("Day")
        verbose_name_plural = _("Days")

    def get_absolute_url(self):
        return reverse('daydetail', args=[self.day])

    @property
    def prettyname(self):
        return ordinal(self.day) + " " + _("day")

    def __str__(self):
        return self.prettyname
