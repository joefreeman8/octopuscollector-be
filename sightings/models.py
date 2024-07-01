from django.db import models


# Create your models here.
class Sighting(models.Model):

    class Meta:
        ordering = ['-date']

    date = models.DateField()
    location = models.CharField(max_length=50)
    # octopus FK
    octopus = models.ForeignKey(
        'octopus.Octopus',
        related_name='octopus',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.octopus} - {self.location} on {self.date}"

    