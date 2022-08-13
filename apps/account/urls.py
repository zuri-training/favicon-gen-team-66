from django.urls import path
from .views import (
  RegisterUserAPIView,
  LoginView, 
  LogoutView,
  UserList,
  # ProfileView,
  UserProfileViewSet,
  RequestPasswordResetEmail,
  PasswordTokenCheckAPIView,
  SetNewPasswordAPIView
  ProfileView,
  ResetPasswordView
  )

urlpatterns = [
  path('register',RegisterUserAPIView.as_view()),
  path('login', LoginView.as_view()),
  path('logout', LogoutView.as_view()),  
  # path('profile', ProfileView.as_view()),
  path('', include(router.urls)),
  path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
  path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPIView.as_view(), name='password-reset-confirm'),
  path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
  path('change_pass', ResetPasswordView.as_view()),
  path('profile', ProfileView.as_view())
]