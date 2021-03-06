# Generated by Django 4.0.5 on 2022-07-05 16:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0009_alter_historicallocation_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicallocation',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, verbose_name='Alias'), blank=True, null=True, size=None, verbose_name='Aliases'),
        ),
        migrations.AddField(
            model_name='location',
            name='aliases',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100, verbose_name='Alias'), blank=True, null=True, size=None, verbose_name='Aliases'),
        ),
    ]
