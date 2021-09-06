from django.db import models

# Create your models here.
from common.models import BaseModel, DescriptionModel


class Location(BaseModel, DescriptionModel):
    part_of = models.ForeignKey("self", on_delete=models.RESTRICT, null=True, blank=True)
