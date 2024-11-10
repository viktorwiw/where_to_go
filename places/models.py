from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.TextField('Название', unique=True)
    short_description = models.TextField('Короткое описание', blank=True)
    long_description = HTMLField('Длинное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, verbose_name='Место', related_name='images')
    image = models.ImageField('Картинка', upload_to='images/')
    position = models.PositiveIntegerField('Позиция', default=0, db_index=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place}'
