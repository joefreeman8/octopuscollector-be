from .common import OctopusSerializer
from sightings.serializers.common import SightingSerializer

class PopulatedOctopusSerializer(OctopusSerializer):
    sightings = SightingSerializer(many=True)