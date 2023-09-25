from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


class NameSlugModel(models.Model):
    name = models.CharField(_("Name"), max_length=1000)
    slug = models.SlugField(editable=False, unique=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.id or True:
            # Newly created object, so set slug
            self.slug = slugify(self.name)
            assert len(self.slug) > 0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
