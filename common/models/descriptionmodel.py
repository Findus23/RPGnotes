from django.db import models

from utils.markdown import md_to_html


class DescriptionModel(models.Model):
    description_md = models.TextField("Description", blank=True)
    description_html = models.TextField("Description (HTML)", blank=True, editable=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.description_html = md_to_html(self.description_md)

        super(DescriptionModel, self).save(*args, **kwargs)
