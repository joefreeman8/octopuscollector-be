from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from .models import Sighting
from .serializers.common import SightingSerializer
from .serializers.populated import PopulatedSightingSerializer

class SightingListView(APIView):

    def get(self, _request):
        sighting = Sighting.objects.all()
        serialized_sighting = PopulatedSightingSerializer(sighting, many=True)
        return Response(serialized_sighting.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        sighting_to_add = SightingSerializer(data=request.data)
        try:
            sighting_to_add.is_valid()
            sighting_to_add.save()
            return Response(sighting_to_add.data, status=status.HTTP_201_CREATED)
        except Exception as e: 
            print('Error')
            return Response(e.__dict__ if e.__dict__ else str(e), status=status.HTTP_422_UNPROCESSABLE_ENTITY)

class SightingDetailView(APIView):

    def get_sighting(self, pk):
        try:
            return Sighting.objects.get(pk=pk)
        except Sighting.DoesNotExist:
            raise NotFound(detail="Can't find that sighting")
        
    def get(self, _request, pk):
        sighting = self.get_sighting(pk=pk)
        serialized_sighting = SightingSerializer(sighting)
        return Response(serialized_sighting.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        sighting_to_edit = self.get_sighting(pk=pk)
        updated_sighting = SightingSerializer(sighting_to_edit, data=request.data)

        if updated_sighting.is_valid():
            updated_sighting.save()
            return Response(updated_sighting.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(updated_sighting.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    def delete(self, request, pk):
        sighting_to_delete = self.get_sighting(pk=pk)
        sighting_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)