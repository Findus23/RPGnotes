# Generated by Django 3.2.7 on 2021-09-23 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0006_auto_20210914_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='character',
            name='description_html',
            field=models.TextField(blank=True, editable=False, verbose_name='Description (HTML)'),
        ),
        migrations.AlterField(
            model_name='character',
            name='description_md',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='historicalcharacter',
            name='description_html',
            field=models.TextField(blank=True, editable=False, verbose_name='Description (HTML)'),
        ),
        migrations.AlterField(
            model_name='historicalcharacter',
            name='description_md',
            field=models.TextField(blank=True, verbose_name='Description'),
        ),
    ]
