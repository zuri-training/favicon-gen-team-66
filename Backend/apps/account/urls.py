from django.urls import path
from .views import (
  RegisterUserAPIView,
  LoginView, 
  LogoutView,
  ProfileView,
  ResetPasswordView
  )

urlpatterns = [
  path('register',RegisterUserAPIView.as_view()),
  path('login', LoginView.as_view()),
  path('logout', LogoutView.as_view()),  
  path('change_pass', ResetPasswordView.as_view()),
  path('profile', ProfileView.as_view())
]