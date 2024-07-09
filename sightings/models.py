from django.db import models


# Create your models here.
class Sighting(models.Model):

    SEAS_OPTIONS = [
        ('Atlantic Ocean', 'Atlantic Ocean'),
        ('Pacific Ocean', 'Pacific Ocean'),
        ('Indian Ocean', 'Indian Ocean'),
        ('Arctic Ocean', 'Arctic Ocean'),
        ('Southern Ocean', 'Southern Ocean'),
        ('Carribean Sea', 'Carribean Sea'),
        ('Philippine Sea', 'Philippine Sea'),
        ('Coral Sea', 'Coral Sea'),
        ('Mediterranean Sea', 'Mediterranean Sea'),
        ('Gulf of Mexico', 'Gulf of Mexico'),
        ('Gulf of Thailand', 'Gulf of Thailand'),
        ('Bay of Bengal', 'Bay of Bengal'),
        ('Java Sea', 'Java Sea'),
        ('Red Sea', 'Red Sea'),
    ]

    class Meta:
        ordering = ['-date']

    date = models.DateField()
    location = models.CharField(max_length=50, choices=SEAS_OPTIONS)
    # octopus FK
    octopus = models.ForeignKey(
        'octopus.Octopus',
        related_name='sightings',
        on_delete=models.CASCADE
    )
    sighting_owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='sightings',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.octopus} - {self.location} on {self.date}"

    