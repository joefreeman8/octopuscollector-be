from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Octopus, Photo, Sighting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'is_staff']


class PhotoSerializer(serializers.ModelSerializer):

    owner = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Photo
        fields = ['id', 'title', 'document', 'created_at',
                  'updated_at', 'octopus_id', 'owner']

    def create(self, validated_data):
        # Extract owner data from validated_data
        owner_data = validated_data.pop('owner')
        # Create Photo instance
        photo = Photo.objects.create(**validated_data)
        # Assign owner to the created photo
        photo.owner = owner_data
        photo.save()
        return photo


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

    sightings_this_week = serializers.SerializerMethodField()

    def get_sightings_this_week(self, obj):
        return obj.sightings_this_week()

    sightings_this_month = serializers.SerializerMethodField()

    def get_sightings_this_month(self, obj):
        return obj.sightings_this_month()

    class Meta:
        model = Octopus
        fields = ['id', 'name', 'scientific_name', 'description',
                  'life_span', 'photos', 'sightings', 'sightings_this_week', 'sightings_this_month']
