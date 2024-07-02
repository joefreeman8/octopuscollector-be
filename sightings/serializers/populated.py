from .common import SightingSerializer
from octopus.serializers.common import OctopusSerializer

class PopulatedSightingSerializer(SightingSerializer):
    octopus = OctopusSerializer()