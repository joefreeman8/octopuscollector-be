from rest_framework import serializers
from ..models import Octopus

class OctopusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Octopus
        fields = ['id', 'name', 'scientific_name', 'description',
                  'life_span', 'sightings', 'sightings_this_week', 'sightings_this_month', 'owner']

