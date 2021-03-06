# Generated by Django 3.2.7 on 2021-09-15 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20210915_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicallocation',
            name='part_of',
        ),
        migrations.RemoveField(
            model_name='location',
            name='part_of',
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='parent',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='locations.location', verbose_name='part of'),
        ),
        migrations.AddField(
            model_name='location',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='locations.location', verbose_name='part of'),
        ),
    ]
