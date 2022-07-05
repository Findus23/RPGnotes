from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField
from tree_queries.fields import TreeNodeForeignKey
from tree_queries.models import TreeNode

from common.models import NameSlugModel, DescriptionModel, HistoryModel, AliasModel
from search.utils import NameSearchIndex
from utils.random_filename import get_file_path


class Location(TreeNode, NameSlugModel, DescriptionModel, AliasModel, HistoryModel):
    parent = TreeNodeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name=_("Part of"),
        related_name="children",
    )
    image = ImageField(_("Image"), upload_to=get_file_path, blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Location")
        verbose_name_plural = _("Locations")
        indexes = [
            NameSearchIndex
        ]

    def get_absolute_url(self):
        return reverse('locationdetail', args=[self.slug])
