from .common import SightingSerializer
from octopus.serializers.common import OctopusSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedSightingSerializer(SightingSerializer):
    octopus = OctopusSerializer()
    owner = UserSerializer()