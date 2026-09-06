from django.db import models
from django.utils import timezone


class Event(models.Model):
    CATEGORY_CHOICES = [
        ("Workshop", "Workshop"),
        ("Competition", "Competition"),
        ("Hackathon", "Hackathon"),
        ("Science Fair", "Science Fair"),
        ("Seminar", "Seminar"),
        ("Exhibition", "Exhibition"),
        ("Training", "Training"),
        ("Robotics", "Robotics"),
        ("AI", "AI"),
        ("Coding", "Coding"),
        ("Engineering", "Engineering"),
        ("Other", "Other"),
    ]

    title = models.CharField(max_length=255)

    slug = models.SlugField(
        max_length=280,
        unique=True,
        blank=True,
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default="Other",
    )

    description = models.TextField()

    event_date = models.DateTimeField()

    time = models.CharField(
        max_length=100,
        blank=True,
        default="Time TBA",
    )

    location = models.CharField(
        max_length=255,
        blank=True,
        default="Location TBA",
    )

    poster = models.ImageField(
        upload_to="events/posters/",
        blank=True,
        null=True,
    )

    banner = models.ImageField(
        upload_to="events/banners/",
        blank=True,
        null=True,
    )

    video = models.FileField(
        upload_to="events/videos/",
        blank=True,
        null=True,
    )

    featured = models.BooleanField(default=False)

    registration_open = models.BooleanField(default=False)

    registration_url = models.URLField(
        blank=True,
        null=True,
    )

    participants_count = models.PositiveIntegerField(
        default=0
    )

    achievements = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["event_date"]

    def __str__(self):
        return self.title

    @property
    def is_past(self):
        return self.event_date < timezone.now()


class EventGallery(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="gallery",
    )

    image = models.ImageField(
        upload_to="events/gallery/"
    )

    alt = models.CharField(
        max_length=255,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.event.title} - Gallery"


class Testimonial(models.Model):
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name="testimonials",
        blank=True,
        null=True,
    )

    name = models.CharField(
        max_length=150
    )

    role = models.CharField(
        max_length=150,
        blank=True,
    )

    comment = models.TextField()

    avatar = models.ImageField(
        upload_to="events/testimonials/",
        blank=True,
        null=True,
    )

    active = models.BooleanField(
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name