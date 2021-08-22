from django.db import models
from django.utils.text import slugify

from notes.models import Campaign


class BaseModel(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.PROTECT)
    name = models.CharField(max_length=1000)
    slug = models.SlugField(editable=False)

    class Meta:
        abstract = True
        unique_together = ["campaign", "slug"]

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(BaseModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
