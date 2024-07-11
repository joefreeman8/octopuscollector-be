from django.db import models

# Create your models here.
class Image(models.Model):
    title = models.CharField(max_length=255)
    document = models.FileField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    octopus = models.ForeignKey(
        'octopus.Octopus',
        related_name='imagess',
        on_delete=models.CASCADE
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Image for octopus_id: {self.octopus_id} @{self.document}"