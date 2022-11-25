from django.db import models
from django.utils.translation import gettext_lazy as _

from utils.markdown import md_to_html


class DescriptionModel(models.Model):
    description_md = models.TextField(_("Description"), blank=True)
    description_html = models.TextField(_("Description (HTML)"), blank=True, editable=False)
    linked_objects = models.TextField(max_length=1000, blank=True, default="")

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.description_html, linked_objects = md_to_html(self.description_md)
        self.linked_objects = ",".join(linked_objects)

        super(DescriptionModel, self).save(*args, **kwargs)
