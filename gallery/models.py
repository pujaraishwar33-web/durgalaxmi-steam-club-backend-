from django.db import models

class Gallery(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to="gallery/")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title