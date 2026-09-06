from rest_framework import serializers

from .models import (
    Event,
    EventGallery,
    Testimonial,
)


class EventGallerySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = EventGallery
        fields = [
            "id",
            "image",
            "image_url",
            "alt",
        ]

    def get_image_url(self, obj):
        request = self.context.get("request")

        if not obj.image:
            return None

        url = obj.image.url

        if request:
            return request.build_absolute_uri(url)

        return url


class TestimonialSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = [
            "id",
            "name",
            "role",
            "comment",
            "avatar",
            "avatar_url",
        ]

    def get_avatar_url(self, obj):
        request = self.context.get("request")

        if not obj.avatar:
            return None

        url = obj.avatar.url

        if request:
            return request.build_absolute_uri(url)

        return url


class EventSerializer(serializers.ModelSerializer):
    gallery = EventGallerySerializer(
        many=True,
        read_only=True,
    )

    testimonials = serializers.SerializerMethodField()

    poster_url = serializers.SerializerMethodField()
    banner_url = serializers.SerializerMethodField()
    video_url = serializers.SerializerMethodField()

    is_past = serializers.ReadOnlyField()

    class Meta:
        model = Event

        fields = [
            "id",
            "slug",

            "title",
            "category",
            "description",

            "event_date",
            "time",
            "location",

            "poster",
            "poster_url",

            "banner",
            "banner_url",

            "video",
            "video_url",

            "featured",

            "registration_open",
            "registration_url",

            "participants_count",
            "achievements",

            "is_past",

            "gallery",
            "testimonials",

            "active",
            "created_at",
            "updated_at",
        ]

    def get_file_url(self, obj, field):
        request = self.context.get("request")

        file = getattr(obj, field, None)

        if not file:
            return None

        url = file.url

        if request:
            return request.build_absolute_uri(url)

        return url

    def get_poster_url(self, obj):
        return self.get_file_url(obj, "poster")

    def get_banner_url(self, obj):
        return self.get_file_url(obj, "banner")

    def get_video_url(self, obj):
        return self.get_file_url(obj, "video")

    def get_testimonials(self, obj):
        queryset = obj.testimonials.filter(
            active=True
        )

        return TestimonialSerializer(
            queryset,
            many=True,
            context=self.context,
        ).data