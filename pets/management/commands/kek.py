import json
import sys

from django.core.management.base import BaseCommand

from pets.models import Pet, Photos
from pets.serializers import PetSerializer
from pets_accounting.settings import PROJECT_BASE_URL


class MockRequest:
    @staticmethod
    def build_absolute_uri(photo_url):
        return PROJECT_BASE_URL + photo_url


class Command(BaseCommand):
    @staticmethod
    def add_arguments(parser):
        parser.add_argument(
            '--has-photos',
            help="Получить всех питомцев в JSON'е",
            type=str,
            required=False,
        )

    @staticmethod
    def handle(*args, **options):
        has_photos = options.get('has_photos')
        pet_with_photo_ids = [i['pet_id'] for i in Photos.objects.values('pet_id').distinct()]
        match has_photos:
            case 'true':
                queryset = Pet.objects.filter(id__in=pet_with_photo_ids)
            case 'false':
                queryset = Pet.objects.exclude(id__in=pet_with_photo_ids)
            case _:
                queryset = Pet.objects.all()
        serializer = PetSerializer(instance=queryset, many=True, context={'request': MockRequest()})
        for item in serializer.data:
            item['photos'] = [i['url'] for i in item['photos']]
        sys.stdout.write('{"pets":' + json.dumps(serializer.data) + '}' + '\n')
