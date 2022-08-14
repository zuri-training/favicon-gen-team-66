from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
from .serializer import IconUploadSerializer
from apps.account import models as account_models
from apps.faviconer import models as favicon_models


class UploadIcon(CreateAPIView):
    """ View for icon upload"""
    permission_classes = [IsAuthenticated]
    serializer_class = IconUploadSerializer


class ListFavicons(ListAPIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, username):
        user = account_models.UserProfile.objects.filter(username=username).first()
        if user:
            favicons = favicon_models.Favicon.objects.filter(user=user).all().values()
            return Response({"data": favicons})
