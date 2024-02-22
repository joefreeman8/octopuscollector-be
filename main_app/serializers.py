from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Octopus, Sighting


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class OctopusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Octopus
        fields = '__all__'


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = '__all__'
