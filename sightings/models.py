from django.db import models
from octopus.models import Octopus

# Create your models here.
class Sighting(models.Model):
    date = models.DateField()
    location = models.CharField(max_length=50)
    # octopus FK
    octopus = models.ForeignKey(Octopus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.octopus} - {self.location} on {self.date}"

    class Meta:
        ordering = ['-date']