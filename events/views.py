from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Event, EventGallery, Testimonial
from .serializers import (
    EventSerializer,
    EventGallerySerializer,
    TestimonialSerializer,
)


class EventViewSet(viewsets.ModelViewSet):
    serializer_class = EventSerializer

    def get_queryset(self):
        queryset = (
            Event.objects
            .filter(active=True)
            .prefetch_related(
                "gallery",
                "testimonials",
            )
        )

        category = self.request.query_params.get(
            "category"
        )

        featured = self.request.query_params.get(
            "featured"
        )

        upcoming = self.request.query_params.get(
            "upcoming"
        )

        past = self.request.query_params.get(
            "past"
        )

        if category and category != "All":
            queryset = queryset.filter(
                category__iexact=category
            )

        if featured == "true":
            queryset = queryset.filter(
                featured=True
            )

        if upcoming == "true":
            from django.utils import timezone

            queryset = queryset.filter(
                event_date__gte=timezone.now()
            )

        if past == "true":
            from django.utils import timezone

            queryset = queryset.filter(
                event_date__lt=timezone.now()
            )

        return queryset

    @action(
        detail=False,
        methods=["get"],
        url_path="featured",
    )
    def featured(self, request):
        event = (
            self.get_queryset()
            .filter(featured=True)
            .order_by("event_date")
            .first()
        )

        if not event:
            return Response(
                {
                    "detail": "No featured event found."
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.get_serializer(event)

        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_path="upcoming",
    )
    def upcoming(self, request):
        from django.utils import timezone

        events = (
            self.get_queryset()
            .filter(
                event_date__gte=timezone.now()
            )
            .order_by("event_date")
        )

        serializer = self.get_serializer(
            events,
            many=True,
        )

        return Response(serializer.data)

    @action(
        detail=False,
        methods=["get"],
        url_path="past",
    )
    def past(self, request):
        from django.utils import timezone

        events = (
            self.get_queryset()
            .filter(
                event_date__lt=timezone.now()
            )
            .order_by("-event_date")
        )

        serializer = self.get_serializer(
            events,
            many=True,
        )

        return Response(serializer.data)


class EventGalleryViewSet(
    viewsets.ModelViewSet
):
    queryset = EventGallery.objects.all()
    serializer_class = EventGallerySerializer

    def get_queryset(self):
        queryset = (
            EventGallery.objects
            .select_related("event")
            .all()
        )

        event_id = self.request.query_params.get(
            "event"
        )

        if event_id:
            queryset = queryset.filter(
                event_id=event_id
            )

        return queryset


class TestimonialViewSet(
    viewsets.ModelViewSet
):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get_queryset(self):
        queryset = (
            Testimonial.objects
            .select_related("event")
            .filter(active=True)
        )

        event_id = self.request.query_params.get(
            "event"
        )

        if event_id:
            queryset = queryset.filter(
                event_id=event_id
            )

        return queryset