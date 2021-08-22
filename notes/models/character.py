from django.conf import settings
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from sorl.thumbnail import ImageField

from notes.models import Faction, Location, BaseModel, DescriptionModel
from notes.utils.colors import get_random_color, is_bright_color


class Character(BaseModel, DescriptionModel):
    subtitle = models.CharField(max_length=100, blank=True)
    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    faction = models.ForeignKey(Faction, on_delete=models.PROTECT, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    color = models.CharField(max_length=6, default=get_random_color)
    image = ImageField(upload_to="character_images", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('characterdetail', args=[self.campaign.slug, self.slug])

    def initials(self):
        return "".join([word[0] for word in self.name.split()][:2]).upper()

    def text_color(self):
        return "black" if is_bright_color(self.color) else "white"
