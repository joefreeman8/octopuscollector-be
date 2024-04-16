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
    queryset = Octopus.objects.all().prefetch_related('photo_set', 'sighting_set')
    serializer_class = OctopusSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter the sightings based on the parent octopus ID
        octopus_id = self.kwargs.get('octopus_pk')
        return Sighting.objects.filter(octopus_id=octopus_id)

    def perform_create(self, serializer):
        octopus_id = self.kwargs.get('octopus_pk')
        octopus = Octopus.objects.get(pk=octopus_id)
        serializer.save(octopus=octopus)


class PhotoViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]
    http_method_names = ['get', 'post', 'patch', 'delete']

    def get_queryset(self):
        # `octopus_pk` is the URL keyword argument set by the nested router
        octopus_id = self.kwargs.get('octopus_pk')
        return Photo.objects.filter(octopus_id=octopus_id)

    def perform_create(self, serializer):

        octopus_id = self.kwargs.get('octopus_pk')
        octopus = Octopus.objects.get(pk=octopus_id)
        serializer.save(octopus=octopus)


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
