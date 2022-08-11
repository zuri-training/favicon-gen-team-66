from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
    UploadIcon,
    ListFavicons
)

urlpatterns = [
    path('add', UploadIcon.as_view()),
    path('list/<str:username>', ListFavicons.as_view())
]
