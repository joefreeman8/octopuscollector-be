from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Octopus, Sighting, Photo


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class OctopusSerializer(serializers.ModelSerializer):
    # * nested the photo serializer
    photos = PhotoSerializer(many=True, required=False)

    class Meta:
        model = Octopus
        fields = '__all__'

    def create(self, validated_data):
        photos_data = validated_data.pop('photos', None)
        octopus = Octopus.objects.create(**validated_data)
        if photos_data:
            for photo_data in photos_data:
                Photo.objects.create(octopus=octopus, **photo_data)
        return octopus


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = '__all__'
