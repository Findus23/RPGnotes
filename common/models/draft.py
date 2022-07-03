from django.db import models
from django.utils.translation import gettext_lazy as _

from rpg_notes.settings import AUTH_USER_MODEL


class Draft(models.Model):
    description_md = models.TextField(_("Description"), blank=True)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT,
        related_name="drafts", verbose_name=_("Player")
    )

    def __str__(self):
        # todo: add which object this is a draft of
        return f"{self.created}: {self.author}"

    class Meta:
        get_latest_by = "created"
