from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import (
  RegisterUserAPIView,
  LoginView, 
  LogoutView,
  UserList,
  ProfileView,
  UserProfileViewSet
  )


router=DefaultRouter()
router.register('profile', UserProfileViewSet)

urlpatterns = [
  path('users', UserList.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('login', LoginView.as_view()),
  path('logout', LogoutView.as_view()),  
  # path('profile', ProfileView.as_view()),
  path('', include(router.urls))
]