from django.urls import path,include
from rest_framework.routers import DefaultRouter
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
  )


router=DefaultRouter()
router.register('profile', UserProfileViewSet)

urlpatterns = [
  path('users', UserList.as_view()),
  path('register',RegisterUserAPIView.as_view()),
  path('login', LoginView.as_view()),
  path('logout', LogoutView.as_view()),  
  # path('profile/', ProfileView.as_view()),
  path('', include(router.urls)),
  path('request-reset-email/', RequestPasswordResetEmail.as_view(), name="request-reset-email"),
  path('password-reset/<uidb64>/<token>/',PasswordTokenCheckAPIView.as_view(), name='password-reset-confirm'),
  path('password-reset-complete', SetNewPasswordAPIView.as_view(),name='password-reset-complete')
]