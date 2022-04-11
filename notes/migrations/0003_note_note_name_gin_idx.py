# Generated by Django 4.0.3 on 2022-04-11 18:54

import django.contrib.postgres.indexes
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20211007_2258'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='note',
            index=django.contrib.postgres.indexes.GinIndex(fields=['name'], name='note_name_gin_idx', opclasses=['gin_trgm_ops']),
        ),
    ]