from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.utils.translation import gettext_lazy as _


class AliasModel(models.Model):
    aliases = ArrayField(
        models.CharField(_("Alias"), max_length=100),
        verbose_name=_("Aliases"), blank=True, null=True
    )

    class Meta:
        abstract = True
