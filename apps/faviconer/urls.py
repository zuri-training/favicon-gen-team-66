from django.urls import path,include
from .views import (
    UploadIcon,
    ListFavicons
)

urlpatterns = [
    path('add', UploadIcon.as_view()),
    path('list/<str:username>', ListFavicons.as_view())
]
