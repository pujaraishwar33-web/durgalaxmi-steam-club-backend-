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
            return url.replace("http://", "https://")
        except Exception:
            return None