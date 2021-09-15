from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField

from common.models import NameSlugModel, DescriptionModel, HistoryModel
from locations.models import Location
from rpg_notes.settings import AUTH_USER_MODEL
from utils.colors import get_random_color, is_bright_color
from utils.random_filename import get_file_path


def validate_color_hex(value: str):
    if not value.startswith("#"):
        raise ValidationError("color hex has to start with a #")


class Character(NameSlugModel, DescriptionModel, HistoryModel):
    subtitle = models.CharField(max_length=100, blank=True)
    player = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True,
                               related_name="characters")
    # faction = models.ForeignKey(Faction, on_delete=models.PROTECT, blank=True, null=True)
    location = models.ForeignKey(Location, on_delete=models.PROTECT, blank=True, null=True)
    color = models.CharField(max_length=7, default=get_random_color, validators=[
        MinLengthValidator(7),
        validate_color_hex
    ])
    token_image = ImageField(upload_to=get_file_path, blank=True, null=True)
    large_image = ImageField(upload_to=get_file_path, blank=True, null=True)

    class Meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse('characterdetail', args=[self.slug])

    def initials(self):
        return "".join([word[0] for word in self.name.split()][:2]).upper()

    def text_color(self):
        return "black" if is_bright_color(self.color) else "white"

    def larger_image(self):
        if self.large_image:
            return self.large_image
        return self.token_image

    def smaller_image(self):
        if self.token_image:
            return self.token_image
        return self.larger_image
