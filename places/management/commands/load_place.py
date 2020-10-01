from django.core.management.base import BaseCommand
from places.models import Place, Image
import requests
from django.core.files.base import ContentFile


class Command(BaseCommand):
    help = 'Загружаем локации и картинки в БД'

    def add_arguments(self, parser):
        parser.add_argument('url', type=str)

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        response.raise_for_status()
        response = response.json()

        place = Place.objects.create(title=response['title'],
                                     description_short=response['description_short'],
                                     description_long=response['description_long'],
                                     longitude=response['coordinates']['lng'],
                                     latitude=response['coordinates']['lat'],
                                     place_id=response['title'])

        for image_link in response['imgs']:
            response = requests.get(image_link)
            imagefile = ContentFile(response.content)
            filename = image_link.split('/')[-1]

            image = Image.objects.create(place_image=place)
            image.image.save(filename, imagefile, save=True)
