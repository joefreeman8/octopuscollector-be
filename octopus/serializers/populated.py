from .common import OctopusSerializer
from sightings.serializers.populated import PopulatedSightingSerializer
from images.serializers.populated import PopulatedImageSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedOctopusSerializer(OctopusSerializer):
    sightings = PopulatedSightingSerializer(many=True)
    images = PopulatedImageSerializer(many=True)
    owner = UserSerializer()
    