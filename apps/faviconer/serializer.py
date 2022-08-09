from rest_framework import serializers

from .utils import FaviconGenerator, ImageUtil


class IconUploadSerializer(serializers.Serializer):
    """This is the serializer on receiving an image."""
    source_url = serializers.URLField(
        label="source_url",
    )
    crop_points = serializers.DictField(
        child=serializers.IntegerField(),
        label="crop_points", required=False
    )
    favicon_size = serializers.IntegerField(label="favicon_size", required=False)
    destination_url = serializers.CharField(read_only=True, required=False)

    def validate(self, data):
        image = ImageUtil.download(data.get("source_url"))
        self.fav_gen = FaviconGenerator(image, data.get("crop_points"), icon_size=data.get("favicon_size"))

        if data.get("crop_points"):
            keys = ["left", "top", "bottom", "right"]
            for key in keys:
                if key not in data.get("crop_points"):
                    raise serializers.ValidationError(f'crop_points: {key} key is missing.')

            is_valid, message = self.fav_gen.validate_crop_points()

            if not is_valid:
                raise serializers.ValidationError(f'crop_points: {message}')

        return data

    def create(self, validated_data):
        self.fav_gen.crop()
        favicon, _ = self.fav_gen.generate()

        destination = ImageUtil.upload(favicon)

        validated_data["destination_url"] = destination
        return validated_data
