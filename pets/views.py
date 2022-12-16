import uuid

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from .models import Pet, Photos
from .serializers import PetSerializer, PhotoSerializer


class PetView(APIView, LimitOffsetPagination):

    def get(self, request):
        pet_with_photo_ids = [i['pet_id'] for i in Photos.objects.values('pet_id').distinct()]
        match request.GET.get('photos'):
            case 'true':
                queryset = Pet.objects.filter(id__in=pet_with_photo_ids)
            case 'false':
                queryset = Pet.objects.exclude(id__in=pet_with_photo_ids)
            case _:
                queryset = Pet.objects.all()
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = PetSerializer(instance=results, many=True, context={'request': request})
        return Response(serializer.data)

    @staticmethod
    def post(request):
        new_pet = request.data
        serializer = PetSerializer(data=new_pet)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)

    @staticmethod
    def delete(request):
        pet_ids = request.data.get('ids')
        if not pet_ids:
            return Response(data="Argument 'ids' in request's body is missing.", status=404)

        deleted_counter = 0
        errors = []
        for pet_id in pet_ids:
            try:
                uuid.UUID(str(pet_id))
            except ValueError:
                errors.append(dict(id=pet_id, error='Unacceptable ID value.'))
                continue
            pet = Pet.objects.filter(id=str(pet_id))
            if pet:
                pet.delete()
                deleted_counter += 1
            else:
                errors.append(dict(id=pet_id, error="Pet with matching ID wasn't found."))

        return Response(data=dict(deleted=deleted_counter, error=errors), status=204)


class PhotoView(APIView):

    @staticmethod
    def post(request, pet_id: str):
        new_photo = request.FILES.get('file')
        serializer = PhotoSerializer(
            data={'pet_id': pet_id, 'url': new_photo}, context={"request": request}
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
        return Response(serializer.data)
