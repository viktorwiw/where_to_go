from django.db import models


class Place(models.Model):
    title = models.TextField('Название')
    description_short = models.CharField('Короткое описание', max_length=250, blank=True)
    description_long = models.CharField('Длинное описание', max_length=200, blank=True)
    latitude = models.FloatField('Широта')
    longtitude = models.FloatField('Долгота')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField('Фотография')
    position = models.PositiveIntegerField('Позиция', unique=True, null=True)

    def __str__(self):
        return f'{self.position} {self.place}'
