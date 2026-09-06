from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Event


class EventAPITestCase(APITestCase):

    def setUp(self):
        self.event = Event.objects.create(
            title="National Robotics Workshop",
            date=timezone.now() + timezone.timedelta(days=30),
            time="9:00 AM - 5:00 PM",
            location="STEAM Innovation Lab",
            category="Robotics",
            description="Robotics workshop.",
            featured=True,
            registration_open=True,
        )

    def test_event_list(self):
        response = self.client.get(
            reverse("events-list")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_upcoming_events(self):
        response = self.client.get(
            reverse("events-upcoming")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_featured_event(self):
        response = self.client.get(
            reverse("events-featured")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_categories(self):
        response = self.client.get(
            reverse("events-categories")
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )