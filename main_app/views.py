from django.contrib.auth.models import User
from rest_framework import viewsets, permissions, status, parsers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .serializers import *

from .models import Photo
import boto3
import uuid
import os
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OctopusViewSet(viewsets.ModelViewSet):
    queryset = Octopus.objects.all()
    serializer_class = OctopusSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # @action(detail=True, methods=['POST'])
    # def add_photo(self, request, pk=None):
    #     octopus = self.get_object()
    #     photo_file = request.FILES.get('photo-file', None)
    #     if photo_file:
    #         s3 = boto3.client('s3')
    #         key = uuid.uuid4().hex[:6] + \
    #             photo_file.name[photo_file.name.rfind('.'):]
    #         try:
    #             bucket = os.environ['S3_BUCKET']
    #             s3.upload_fileobj(photo_file, bucket, key)
    #             url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
    #             Photo.objects.create(url=url, octopus=octopus)
    #             return Response({'status': 'photo added'}, status=status.HTTP_201_CREATED)
    #         except Exception as e:
    #             return Response({'status': 'error uploading to S3', 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    #     return Response({'status': 'no file provided'}, status=status.HTTP_400_BAD_REQUEST)


class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter the sightings based on the parent octopus ID
        octopus_id = self.kwargs.get('octopus_pk')
        return Sighting.objects.filter(octopus_id=octopus_id)


# class PhotoViewSet(viewsets.ModelViewSet):
#     serializer_class = PhotoSerializer

#     def get_queryset(self):
#         # `octopus_pk` is the URL keyword argument set by the nested router
#         octopus_id = self.kwargs.get('octopus_pk')
#         return Photo.objects.filter(octopus_id=octopus_id)

#     def perform_create(self, serializer):
#         octopus_id = self.kwargs.get('octopus_pk')
#         octopus = Octopus.objects.get(pk=octopus_id)
#         serializer.save(octopus=octopus)


class PhotoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']


class LogoutView(APIView):
    # permission_classes = (IsAuthenticated, )

    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignupView(APIView):

    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        try:
            new_user = User.objects.create(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
