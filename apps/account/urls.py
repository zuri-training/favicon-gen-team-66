from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
  RegisterUserAPIView,
  LoginView, 
  LogoutView,
  # ProfileView,
  UserProfileView,
  # UserProfileViewSet
  )


# router=DefaultRouter()
# router.register('profile', UserProfileViewSet)

urlpatterns = [
  path('register',RegisterUserAPIView.as_view()),
  path('login', LoginView.as_view()),
  path('logout', LogoutView.as_view()),
  path('userprofile', UserProfileView.as_view()),
  # path('', include(router.urls))
]