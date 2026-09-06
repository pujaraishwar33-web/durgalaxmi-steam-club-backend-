from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    EventViewSet,
    EventGalleryViewSet,
    TestimonialViewSet,
)


router = DefaultRouter()

router.register(
    r"",
    EventViewSet,
    basename="event",
)

router.register(
    r"gallery",
    EventGalleryViewSet,
    basename="event-gallery",
)

router.register(
    r"testimonials",
    TestimonialViewSet,
    basename="testimonial",
)


urlpatterns = [
    path(
        "",
        include(router.urls)
    ),
]