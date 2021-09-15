from django.db import models
# Create your models here.
from django.urls import reverse
from tree_queries.fields import TreeNodeForeignKey
from tree_queries.models import TreeNode

from common.models import NameSlugModel, DescriptionModel, HistoryModel


class Location(TreeNode, NameSlugModel, DescriptionModel, HistoryModel):
    parent = TreeNodeForeignKey(
        "self",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="part of",
        related_name="children",
    )

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('locationdetail', args=[self.slug])
