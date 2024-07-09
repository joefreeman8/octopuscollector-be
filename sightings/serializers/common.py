from rest_framework import serializers
from ..models import Sighting


class SightingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sighting
        fields = '__all__'

    date = serializers.DateField(error_messages={
        'required': 'Please enter a valid date',
        'blank': 'Please enter a valid date',
        'invalid': 'Please enter a valid date'
    })
    
    def validate_location(self, value):
        valid_locations = [sea[0] for sea in Sighting.SEAS_OPTIONS]
        if value not in valid_locations:
            raise serializers.ValidationError(f"{value} is not a valid choice.")
        return value