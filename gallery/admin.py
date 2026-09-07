from django.contrib import admin

from .models import Gallery


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "category",
        "uploaded_at",
    )

    list_filter = (
        "category",
        "uploaded_at",
    )

    search_fields = (
        "title",
        "description",
        "category",
    )

    ordering = (
        "-uploaded_at",
    )