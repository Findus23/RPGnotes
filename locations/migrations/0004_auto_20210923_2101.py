# Generated by Django 3.2.7 on 2021-09-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_auto_20210915_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallocation',
            name='description_html',
            field=models.TextField(blank=True, editable=False, verbose_name='Description (HTML)'),
        ),
        migrations.AlterField(
            model_name='historicallocation',
            name='description_md',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description_html',
            field=models.TextField(blank=True, editable=False, verbose_name='Description (HTML)'),
        ),
        migrations.AlterField(
            model_name='location',
            name='description_md',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
