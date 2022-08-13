# from django.shortcuts import render
from rest_framework.response import Response

# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
)
# from rest_framework import serializers
from rest_framework.permissions import AllowAny

from .serializer import IconUploadSerializer
from apps.account import models as account_models
from apps.faviconer import models as favicon_models


class UploadIcon(CreateAPIView):
    """ View for icon upload"""
    # TODO: Remove AllowAny and require authorization.
    permission_classes = [AllowAny]
    serializer_class = IconUploadSerializer


class ListFavicons(ListAPIView):
    permission_classes = [AllowAny]
    def get(self, request, username):
        user = account_models.UserProfile.objects.filter(username=username).first()
        if user:
            favicons = favicon_models.Favicon.objects.filter(user=user).all().values()
            return Response({"data": favicons})
