from django.urls import path
from .views import UserDetailAPIView,RegisterUserAPIView


urlpatterns = [
  path("get-details",UserDetailAPIView.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]