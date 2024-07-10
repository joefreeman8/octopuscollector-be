from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status

from .models import Octopus
from .serializers.common import OctopusSerializer
from .serializers.populated import PopulatedOctopusSerializer
from .permissions import IsAdminOrReadOnly


class OctopusListView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

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



class OctopusDetailView(APIView):
    permission_classes = (IsAdminOrReadOnly, )

    def get_octopus(self, pk):
        try:
            return Octopus.objects.get(pk=pk)
        except Octopus.DoesNotExist:
            raise NotFound(detail="Can't find this Octopus, are you sure it exists?")
        
    def get(self, _request, pk):
            single_octopus = self.get_octopus(pk=pk)
            serialized_single_octopus = PopulatedOctopusSerializer(single_octopus)
            return Response(serialized_single_octopus.data, status=status.HTTP_200_OK)
            
    def put(self, request, pk):
        octopus_to_edit = self.get_octopus(pk=pk)
        request.data['owner'] = request.user.id
        update_octopus = OctopusSerializer(octopus_to_edit, data=request.data)
        
        if update_octopus.is_valid():
            update_octopus.save()
            return Response(update_octopus.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(update_octopus.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        

    def delete(self, _request, pk):
        octopus_to_delete = self.get_octopus(pk=pk)
        octopus_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)