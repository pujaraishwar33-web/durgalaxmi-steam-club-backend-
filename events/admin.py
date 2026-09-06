from django.contrib import admin

from .models import (
    Event,
    EventGallery,
    Testimonial,
)


class EventGalleryInline(admin.TabularInline):
    model = EventGallery
    extra = 1


class TestimonialInline(admin.TabularInline):
    model = Testimonial
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "category",
        "event_date",
        "location",
        "featured",
        "registration_open",
        "active",
    )

    list_filter = (
        "category",
        "featured",
        "registration_open",
        "active",
    )

    search_fields = (
        "title",
        "description",
        "location",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    inlines = [
        EventGalleryInline,
        TestimonialInline,
    ]

    ordering = (
        "event_date",
    )


@admin.register(EventGallery)
class EventGalleryAdmin(admin.ModelAdmin):
    list_display = (
        "event",
        "alt",
        "created_at",
    )

    list_filter = (
        "event",
    )

    search_fields = (
        "event__title",
        "alt",
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "role",
        "event",
        "active",
        "created_at",
    )

    list_filter = (
        "active",
        "event",
    )

    search_fields = (
        "name",
        "comment",
        "role",
    )

    readonly_fields = (
        "created_at",
    )