from django.db import models
from datetime import timedelta
from django.utils.timezone import now


class Octopus(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    life_span = models.IntegerField()
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='octopus',
        on_delete=models.CASCADE
    )

    def sightings_this_week(self):
        one_week_ago = now() - timedelta(days=7)
        return self.sightings.filter(date__gt=one_week_ago).count()

    def sightings_this_month(self):
        today = now().date()
        one_week_ago = today - timedelta(days=7)
        one_month_ago = today - timedelta(days=28)

        # Filter sightings that are older than a week but less than a month
        sightings = self.sightings.filter(
            date__gt=one_month_ago, date__lte=one_week_ago).count()
        return sightings

    def __str__(self):
        return self.name
