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


# class SightingViewSet(viewsets.ModelViewSet):
#     queryset = Sighting.objects.all()
#     serializer_class = SightingSerializer
#     permision_classes = [permissions.IsAuthenticatedOrReadOnly]


class SightingViewSet(viewsets.ModelViewSet):
    serializer_class = SightingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Optionally restricts the returned sightings to a given octopus,
        by filtering against a `octopus_id` query parameter in the URL.
        """
        queryset = Sighting.objects.all()
        lookup_field = 'pk'
        # `octopus_pk` matches the lookup field from the router
        octopus_id = self.kwargs.get('octopus_pk')
        if octopus_id is not None:
            queryset = queryset.filter(octopus_id=octopus_id)
        return queryset
