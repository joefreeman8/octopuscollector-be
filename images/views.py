from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Image
from octopus.models import Octopus

from .serializers import ImageSerializer

class ImageListView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def get(self, _request, octopus_pk):
        images = Image.objects.filter(octopus_id=octopus_pk)
        serialized_images = ImageSerializer(images, many=True)
        return Response(serialized_images.data, status=status.HTTP_200_OK)

    def post(self, request, octopus_pk):
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
    parser_classes = [MultiPartParser, FormParser]

    def get_image(self, pk):
        try:
            return Image.objects.get(pk=pk)
        except Image.DoesNotExist:
            raise NotFound(detail="Image not found")

    def get(self, request, octopus_pk, pk):
        image = self.get_image(pk)
        if image.octopus_id != octopus_pk:
            return Response({'detail': 'Image not associated with this octopus'}, status=status.HTTP_404_NOT_FOUND)
        serialized_image = ImageSerializer(Image)
        return Response(serialized_image.data, status=status.HTTP_200_OK)

    def put(self, request, octopus_pk, pk):
        image = self.get_Image(pk)
        if image.octopus_id != octopus_pk:
            return Response({'detail': 'Image not associated with this octopus'}, status=status.HTTP_404_NOT_FOUND)
        image_to_update = ImageSerializer(image, data=request.data, partial=True)
        if image_to_update.is_valid():
            image_to_update.save()
            return Response(image_to_update.data, status=status.HTTP_202_ACCEPTED)
        return Response(image_to_update.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def delete(self, _request, octopus_pk, pk):
        image = self.get_Image(pk)
        if image.octopus_id != octopus_pk:
            return Response({'detail': 'Image not associated with this octopus'}, status=status.HTTP_404_NOT_FOUND)
        image.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
