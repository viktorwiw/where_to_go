# Generated by Django 4.2.13 on 2024-11-10 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_remove_place_title_short'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='description_long',
            new_name='long_description',
        ),
        migrations.RenameField(
            model_name='place',
            old_name='description_short',
            new_name='short_description',
        ),
    ]
