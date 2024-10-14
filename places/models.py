from django.db import models


class Place(models.Model):
    title = models.TextField('Название')
    title_short = models.TextField('Краткое название', null=True)
    description_short = models.CharField('Короткое описание', max_length=250, blank=True)
    description_long = models.CharField('Длинное описание', max_length=200, blank=True)
    longitude = models.FloatField('Долгота')
    latitude = models.FloatField('Широта')

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    image = models.ImageField('Фотография', upload_to='images/')
    position = models.PositiveIntegerField('Позиция', unique=True, null=True)

    def __str__(self):
        return f'{self.position} {self.place}'
