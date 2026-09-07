from rest_framework import viewsets
from rest_framework.parsers import (
    MultiPartParser,
    FormParser,
)

from .models import Gallery
from .serializers import GallerySerializer


class GalleryViewSet(viewsets.ModelViewSet):

    queryset = Gallery.objects.all().order_by(
        "-uploaded_at"
    )

    serializer_class = GallerySerializer

    parser_classes = [
        MultiPartParser,
        FormParser,
    ]