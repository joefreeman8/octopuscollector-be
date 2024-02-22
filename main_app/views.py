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


class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        # Filter the sightings based on the parent octopus ID
        octopus_id = self.kwargs.get('octopus_pk')
        return Sighting.objects.filter(octopus_id=octopus_id)
