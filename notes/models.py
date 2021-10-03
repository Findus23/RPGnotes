from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from tree_queries.fields import TreeNodeForeignKey
from tree_queries.models import TreeNode

from common.models import NameSlugModel, DescriptionModel, HistoryModel


class Note(TreeNode, NameSlugModel, DescriptionModel, HistoryModel):
    parent = TreeNodeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Part of"),
        related_name="children",
    )

    class Meta:
        ordering = ["name"]
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def get_absolute_url(self):
        return reverse('notedetail', args=[self.slug])
