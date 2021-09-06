from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from simple_history.models import HistoricalRecords
from sorl.thumbnail import ImageField

from common.models import BaseModel, DescriptionModel
from locations.models import Location
from rpg_notes.settings import AUTH_USER_MODEL
from utils.colors import get_random_color, is_bright_color


def validate_color_hex(value: str):
    if not value.startswith("#"):
        raise ValidationError("color hex has to start with a #")


class Character(BaseModel, DescriptionModel):
    subtitle = models.CharField(max_length=100, blank=True)
    player = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True)
    # faction = models.ForeignKey(Faction, on_delete=models.PROTECT, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    color = models.CharField(max_length=7, default=get_random_color, validators=[
        MinLengthValidator(7),
        validate_color_hex
    ])
    image = ImageField(upload_to="character_images", blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('characterdetail', args=[self.slug])

    def initials(self):
        return "".join([word[0] for word in self.name.split()][:2]).upper()

    def text_color(self):
        return "black" if is_bright_color(self.color) else "white"
