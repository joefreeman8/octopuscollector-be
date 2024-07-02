from rest_framework import serializers
from ..models import Octopus

class OctopusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Octopus
        fields = '__all__'

