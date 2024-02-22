from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from .serializers import *
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class OctopusViewSet(viewsets.ModelViewSet):
    queryset = Octopus.objects.all()
    serializer_class = OctopusSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
