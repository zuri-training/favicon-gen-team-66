from rest_framework import serializers

from .utils import FaviconGenerator, ImageUtil, generate_favicon_id
from apps.account import models
from .models import Favicon as FaviconModel


class IconUploadSerializer(serializers.Serializer):
    """This is the serializer on receiving an image."""
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        write_only=True
    )
    source_url = serializers.URLField(
        label="source_url",
    )
    crop_points = serializers.DictField(
        child=serializers.IntegerField(),
        label="crop_points", required=False
    )
    favicon_size = serializers.IntegerField(label="favicon_size", required=False)
    destination_url = serializers.CharField(read_only=True, required=False)

    def validate_user(self, data):
        username = data.get('username')
        password = data.get('password')
        user = models.UserProfile.objects.filter(username=username).first()
        if user.check_password(password):
            return user
        else:
            raise serializers.ValidationError(f'user_details: User does not exist.')

    def validate(self, data):
        self.user = self.validate_user(data)
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
        if validated_data["destination_url"]:
            fav_id = generate_favicon_id(
                validated_data.get("source_url"),
                self.fav_gen.crop_points,
                self.fav_gen.icon_size
            )
            FaviconModel(
                id=fav_id,
                user=self.user,
                source_url=validated_data.get("source_url"),
                size=self.fav_gen.icon_size,
                destination_url=validated_data.get("destination_url")
            ).save()

        return validated_data
