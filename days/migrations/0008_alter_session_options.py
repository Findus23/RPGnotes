# Generated by Django 5.1.4 on 2025-01-03 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("days", "0007_historicalingameday_linked_objects_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="session",
            options={
                "ordering": ["date"],
                "verbose_name": "Session",
                "verbose_name_plural": "Sessions",
            },
        ),
    ]
