from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError
import requests
from urllib.parse import urlparse
from places.models import Place, Image
import logging


logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('url', type=str, help='URL of the place to load')

        parser.add_argument(
            '--timeout',
            type=int,
            help='Request timeout',
            default=3
        )

    def handle(self, *args, **options):
        url = options['url']
        timeout = options['timeout']

        try:
            response = requests.get(url, timeout=timeout)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise CommandError(f'Request failed:{e}')

        location = response.json()

        place, created = Place.objects.get_or_create(
            title=location['title'],
            title_short=location['title'],
            description_short=location['description_short'],
            description_long=location['description_long'],
            longitude=location['coordinates']['lng'],
            latitude=location['coordinates']['lat'],
            )

        for image_url in location['imgs']:
            try:
                image_response = requests.get(image_url, timeout=timeout)
                image_response.raise_for_status()
            except requests.exceptions.HTTPError as e:
                self.stdout.write(f"Ошибка при скачивании изображения по URL {image_url}: {e}")
                continue

            image_name = urlparse(image_url).path.split('/')[-1]
            image_content = ContentFile(image_response.content, name=image_name)

            picture = Image(place=place)
            picture.image.save(image_name, image_content, save=True)

        if created:
            self.stdout.write(self.style.SUCCESS('Новый объект создан'))
        else:
            self.stdout.write(self.style.SUCCESS(f'{location["title"]} - Такой объект уже существует'))
