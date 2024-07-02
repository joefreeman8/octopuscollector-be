from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # Already requires username and password, so just need to add other features.
    email = models.CharField(max_length=60, unique=True)