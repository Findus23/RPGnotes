# Generated by Django 3.2.6 on 2021-08-23 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_auto_20210823_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalsession',
            name='description_html',
        ),
        migrations.RemoveField(
            model_name='historicalsession',
            name='description_md',
        ),
        migrations.RemoveField(
            model_name='session',
            name='description_html',
        ),
        migrations.RemoveField(
            model_name='session',
            name='description_md',
        ),
        migrations.AddField(
            model_name='historicalingameday',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='historicalingameday',
            name='description_md',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='ingameday',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='ingameday',
            name='description_md',
            field=models.TextField(blank=True),
        ),
    ]
