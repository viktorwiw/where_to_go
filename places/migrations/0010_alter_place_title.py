# Generated by Django 4.2.13 on 2024-11-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_alter_place_description_long'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.TextField(unique=True, verbose_name='Название'),
        ),
    ]
