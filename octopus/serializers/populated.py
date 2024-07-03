from .common import OctopusSerializer
from sightings.serializers.populated import PopulatedSightingSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedOctopusSerializer(OctopusSerializer):
    sightings = PopulatedSightingSerializer(many=True)
    owner = UserSerializer()