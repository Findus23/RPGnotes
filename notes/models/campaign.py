from django.conf import settings
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords

from notes.models import DescriptionModel


class Campaign(DescriptionModel):
    name = models.CharField(max_length=1000)
    slug = models.SlugField(unique=True, editable=False)
    dm = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def get_absolute_url(self):
        return reverse('campaigndetail', args=[str(self.slug)])

    def __str__(self):
        return self.name
