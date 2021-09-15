from django.db import models
from django.utils.text import slugify


class NameSlugModel(models.Model):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(editable=False, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id:
            # Newly created object, so set slug
            self.slug = slugify(self.name)

        super(NameSlugModel, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
