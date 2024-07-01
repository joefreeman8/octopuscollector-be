from rest_framework import serializers
from .models import Sighting
from octopus.serializers import OctopusSerializer

class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = '__all__'

class PopulatedSightingSerializer(SightingSerializer):
    octopus = OctopusSerializer()