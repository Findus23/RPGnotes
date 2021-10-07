# Generated by Django 3.2.7 on 2021-10-07 20:58

from django.db import migrations, models
import sorl.thumbnail.fields
import utils.random_filename


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalnote',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='note',
            name='image',
            field=sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=utils.random_filename.get_file_path, verbose_name='Image'),
        ),
    ]
