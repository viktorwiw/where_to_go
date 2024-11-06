from django.db import models
from tinymce.models import HTMLField


class Place(models.Model):
    title = models.TextField('Название', unique=True)
    title_short = models.TextField('Краткое название', null=True)
    description_short = models.CharField('Короткое описание', max_length=250, blank=True)
    description_long = HTMLField('Длинное описание', blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField('Картинка', upload_to='images/')
    position = models.PositiveIntegerField('Позиция', default=0, null=True)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return f'{self.position} {self.place}'
