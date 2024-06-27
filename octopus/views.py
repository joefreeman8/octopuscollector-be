from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Octopus
from .serializers import OctopusSerializer

class OctopusListView(APIView):

    def get(self, _request):
        octopus = Octopus.objects.all()
        serialized_octopus = OctopusSerializer(octopus, many=True)
        return Response(serialized_octopus.data, status=status.HTTP_200_OK)