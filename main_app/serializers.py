from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Octopus, Photo, Sighting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'document', 'created_at',
                  'updated_at', 'octopus_id']


class SightingSerializer(serializers.ModelSerializer):
    # creates a field which isn't in my model
    location_display = serializers.SerializerMethodField()

    # populates the field above from data in model, -> obj refers to the model
    def get_location_display(self, obj):
        return obj.get_location_display()

    class Meta:
        model = Sighting
        fields = ['date', 'location', 'location_display', 'octopus']


class OctopusSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(source='photo_set', many=True, read_only=True)
    sightings = SightingSerializer(
        source='sighting_set', many=True, read_only=True)

    class Meta:
        model = Octopus
        fields = ['id', 'name', 'scientific_name', 'description',
                  'life_span', 'photos', 'sightings']
