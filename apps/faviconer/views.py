from django.shortcuts import render

# Create your views here.
from rest_framework.generics import (
    CreateAPIView,
)
from .serializer import IconUploadSerializer
from rest_framework.permissions import AllowAny


class UploadIcon(CreateAPIView):
    """ View for icon upload"""
    # TODO: Remove AllowAny and require authorization.
    permission_classes = [AllowAny]
    serializer_class = IconUploadSerializer
