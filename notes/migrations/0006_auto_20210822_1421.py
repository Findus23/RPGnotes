# Generated by Django 3.2.6 on 2021-08-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_auto_20210822_1259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='notes',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='notes',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='faction',
            old_name='notes',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='historicalcampaign',
            old_name='notes',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='historicalcharacter',
            old_name='notes',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='historicalfaction',
            old_name='notes',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='historicalloot',
            old_name='description',
            new_name='description_md',
        ),
        migrations.RenameField(
            model_name='loot',
            old_name='description',
            new_name='description_md',
        ),
        migrations.AddField(
            model_name='campaign',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='character',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='faction',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='historicalcampaign',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='historicalcharacter',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='historicalfaction',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='historicallocation',
            name='description_md',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='historicalloot',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='location',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AddField(
            model_name='location',
            name='description_md',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='loot',
            name='description_html',
            field=models.TextField(blank=True, editable=False),
        ),
        migrations.AlterField(
            model_name='historicalloot',
            name='value_gold',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Value (Gold)'),
        ),
        migrations.AlterField(
            model_name='loot',
            name='value_gold',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Value (Gold)'),
        ),
    ]
