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
        fields = ['title', 'document', 'created_at', 'updated_at']


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = ['date', 'location']


class OctopusSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(source='photo_set', many=True, read_only=True)
    sightings = SightingSerializer(
        source='sighting_set', many=True, read_only=True)

    class Meta:
        model = Octopus
        fields = ['id', 'name', 'scientific_name', 'description',
                  'life_span', 'photos', 'sightings']
