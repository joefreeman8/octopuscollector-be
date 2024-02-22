from django.db import models

# Create your models here.


class Octopus(models.Model):
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    life_span = models.IntegerField()

    def __str__(self):
        return self.name
