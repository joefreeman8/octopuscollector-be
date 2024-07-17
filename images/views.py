from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Image
from octopus.models import Octopus

from .serializers.common import ImageSerializer

class ImageListView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )
    parser_classes = [MultiPartParser, FormParser]

    def get(self, _request, octopus_pk):
        images = Image.objects.filter(octopus_id=octopus_pk)
        serialized_images = ImageSerializer(images, many=True)
        return Response(serialized_images.data, status=status.HTTP_200_OK)


    def post(self, request):
        request.data['image_owner'] = request.user.id
        octopus_pk = request.data['octopus']
        try:
            octopus = Octopus.objects.get(pk=octopus_pk)
        except Octopus.DoesNotExist:
            raise NotFound(detail="Octopus not found")

        image_to_add = ImageSerializer(data=request.data)
        
        if image_to_add.is_valid():
            image_to_add.save(octopus=octopus)
            return Response(image_to_add.data, status=status.HTTP_201_CREATED)
        
        return Response(image_to_add.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


class ImageDetailView(APIView):
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_image(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound(detail="Image not found")

    
    def delete(self, _request, pk):
        image_to_delete = self.get_image(pk=pk)
        image_to_delete.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

