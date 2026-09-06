from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Django Admin
    path("admin/", admin.site.urls),

    # Gallery API
    path(
        "api/gallery/",
        include("gallery.urls"),
    ),

    # Contact API
    path(
        "api/contact/",
        include("contact.urls"),
    ),

    # Events API
    path(
        "api/events/",
        include("events.urls"),
    ),
]


# Serve uploaded media files during development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )