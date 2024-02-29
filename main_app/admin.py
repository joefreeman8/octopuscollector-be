from django.contrib import admin
from .models import Octopus, Sighting, Photo

# Register your models here.
admin.site.register(Octopus)
admin.site.register(Sighting)
admin.site.register(Photo)
