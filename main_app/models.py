from django.db import models
from datetime import timedelta
from django.utils.timezone import now

# Create your models here.


class Octopus(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    life_span = models.IntegerField()

    def sightings_this_week(self):
        one_week_ago = now() - timedelta(days=7)
        return self.sighting_set.filter(date__gt=one_week_ago).count()

    def sightings_this_month(self):
        today = now().date()
        one_week_ago = today - timedelta(days=7)
        one_month_ago = today - timedelta(days=28)

        # Filter sightings that are older than a week but less than a month
        sightings = self.sighting_set.filter(
            date__gt=one_month_ago, date__lte=one_week_ago).count()
        return sightings

    def __str__(self):
        return self.name


SEAS = (
    ('ATL', 'Atlantic Ocean'),
    ('PAC', 'Pacific Ocean'),
    ('IND', 'Indian Ocean'),
    ('ARC', 'Arctic Ocean'),
    ('SOU', 'Southern Ocean'),
    ('CAR', 'Carribean Sea'),
    ('PHI', 'Philippine Sea'),
    ('COR', 'Coral Sea'),
    ('MED', 'Mediterranean Sea'),
    ('MEX', 'Gulf Of Mexico'),
    ('THA', 'Gulf Of Thailand'),
    ('BEN', 'Bay Of Bengal'),
    ('JAV', 'Java Sea'),
    ('RED', 'Red Sea')
)


class Sighting(models.Model):
    date = models.CharField('Sighting Date')
    location = models.CharField(
        max_length=3,
        choices=SEAS,
        default=SEAS[0][0]
    )
    # octopus FK
    octopus = models.ForeignKey(Octopus, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_location_display()} on {self.date}"

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    octopus = models.ForeignKey(Octopus, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Photos'

    def __str__(self):
        return f"Photo for octopus_id: {self.octopus_id} @{self.document}"
