from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
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
    subtitle = models.CharField(_("Subtitle"), max_length=100, blank=True)
    player = models.ForeignKey(
        AUTH_USER_MODEL, on_delete=models.PROTECT, blank=True, null=True,
        related_name="characters", verbose_name=_("Player"),
        help_text=_("If no player is selected, this character is considered an NPC.")
    )
    # faction = models.ForeignKey(Faction, on_delete=models.PROTECT, blank=True, null=True)
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, blank=True, null=True,
        verbose_name=_("Location")
    )
    color = models.CharField(_("Color"), max_length=7, default=get_random_color, validators=[
        MinLengthValidator(7),
        validate_color_hex
    ])
    token_image = ImageField(_("Token Image"), upload_to=get_file_path, blank=True, null=True, help_text=_("round"))
    large_image = ImageField(_("Large Image"), upload_to=get_file_path, blank=True, null=True)

    class Meta:
        ordering = ["name"]
        verbose_name = _("Character")
        verbose_name_plural = _("Characters")

    def get_absolute_url(self):
        return reverse('characterdetail', args=[self.slug])

    @property
    def initials(self):
        return "".join([word[0] for word in self.name.split()][:2]).upper()

    @property
    def firstname(self):
        return self.name.split()[0]

    @property
    def text_color(self):
        return "black" if is_bright_color(self.color) else "white"

    @property
    def larger_image(self):
        if self.large_image:
            return self.large_image
        return self.token_image

    @property
    def smaller_image(self):
        if self.token_image:
            return self.token_image
        return self.larger_image
