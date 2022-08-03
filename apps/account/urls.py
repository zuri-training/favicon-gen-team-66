from django.urls import path
from .views import (
  RegisterUserAPIView,
  LoginView, 
  LogoutView,
  UserList,
  ProfileView
  )


urlpatterns = [
  path('users', UserList.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('login', LoginView.as_view()),
  path('logout', LogoutView.as_view()),  
  path('profile/', ProfileView.as_view()),
]