from django.db import models
from cloudinary.models import CloudinaryField


class Gallery(models.Model):

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    category = models.CharField(
        max_length=100
    )

    image = CloudinaryField(
        "image",
        folder="durgalaxmi/gallery"
    )

    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title