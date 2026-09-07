from django.contrib import admin
from django.urls import path, include


urlpatterns = [

    # Django Admin
    path(
        "admin/",
        admin.site.urls
    ),

    # Gallery API
    path(
        "api/gallery/",
        include("gallery.urls")
    ),

    # Contact API
    path(
        "api/contact/",
        include("contact.urls")
    ),

    # Events API
    path(
        "api/events/",
        include("events.urls")
    ),
]