from django.db import models

# Create your models here.
class Image(models.Model):

    class Meta:
        ordering = ['-created_at']

    title = models.CharField(max_length=255)
    document = models.FileField(max_length=255)
    created_at = models.DateField()
    octopus = models.ForeignKey(
        'octopus.Octopus',
        related_name='images',
        on_delete=models.CASCADE
    )
    image_owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='images',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Image for octopus_id: {self.octopus_id} @{self.document}"