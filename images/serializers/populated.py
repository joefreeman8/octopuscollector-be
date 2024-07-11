from .common import ImageSerializer
from jwt_auth.serializers import UserSerializer

class PopulatedImageSerializer(ImageSerializer):
    image_owner = UserSerializer()