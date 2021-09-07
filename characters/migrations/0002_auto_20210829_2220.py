# Generated by Django 3.2.6 on 2021-08-29 20:20

import characters.models
import django.core.validators
from django.db import migrations, models
import utils.colors


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='color',
            field=models.CharField(default=utils.colors.get_random_color, max_length=7, validators=[django.core.validators.MinLengthValidator(7), characters.models.validate_color_hex]),
        ),
        migrations.AlterField(
            model_name='historicalcharacter',
            name='color',
            field=models.CharField(default=utils.colors.get_random_color, max_length=7, validators=[django.core.validators.MinLengthValidator(7), characters.models.validate_color_hex]),
        ),
    ]