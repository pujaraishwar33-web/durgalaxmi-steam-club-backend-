from rest_framework import serializers
from .models import Gallery


class GallerySerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Gallery
        fields = "__all__"

    def get_image(self, obj):
        if not obj.image:
            return None

        try:
            url = obj.image.url

            # Always use HTTPS for Cloudinary
            if url.startswith("http://"):
                url = url.replace("http://", "https://", 1)

            return url

        except Exception:
            return None