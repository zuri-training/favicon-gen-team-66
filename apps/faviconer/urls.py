from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
 UploadIcon
)


# router=DefaultRouter()
# router.register('profile', UserProfileViewSet)
#
urlpatterns = [
  path('add', UploadIcon.as_view()),
  # path('get',RegisterUserAPIView.as_view()),
]
