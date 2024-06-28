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
    
    def post(self, request):
        octopus_to_add = OctopusSerializer(data=request.data)
        try:
            octopus_to_add.is_valid()
            octopus_to_add.save()
            return Response(octopus_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e: 
            print('Error')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
