from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from .models import Sighting
from .serializers import SightingSerializer, PopulatedSightingSerializer

class SightingListView(APIView):

    def get(self, _request):
        sighting = Sighting.objects.all()
        serialized_sighting = PopulatedSightingSerializer(sighting, many=True)
        return Response(serialized_sighting.data, status=status.HTTP_200_OK)
    
    # def post(self, request):
    #     sighting_to_add = SightingSerializer(data=request.data)
    #     try:
    #         sighting_to_add.is_valid()
    #         sighting_to_add.save()
    #         return Response(sighting_to_add.data, status=status.HTTP_201_CREATED)
    #     except Exception as e: 
    #         print('Error')
    #         return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)
