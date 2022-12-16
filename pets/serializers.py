from rest_framework import serializers

from pets.models import Pet, Photos


class PhotoSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False, format='hex_verbose')
    url = serializers.ImageField(use_url=True)

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)

    class Meta:
        model = Photos
        fields = ['id', 'pet_id', 'url']
        extra_kwargs = {
            'pet_id': {'write_only': True},
        }


class PetSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(required=False, format='hex_verbose')
    photos = PhotoSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = Pet
        fields = ['id', 'name', 'age', 'type', 'photos', 'created_at']
