from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from django.conf import settings
from . import models
from .serializer import (
    UserSerializer, 
    RegisterSerializer,
    UserProfileSerializer,
    UpdatedLoginSerializer,
    ResetPasswordSerializer,
    UpdateUserSerializer
    )
from .permissions import (
    IsCreatorOrAdmin,
    UpdateOwnProfile,
)
from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
    )
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

User = settings.AUTH_USER_MODEL

#Class based view to register user
class RegisterUserAPIView(CreateAPIView):
    """ View for user registration"""
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer
   
class LoginView(APIView):
    """ view for user login """
    permission_classes = [AllowAny]
    serializer_class = UpdatedLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(
            data=self.request.data,
            context={ 'request': self.request }
            )
        serializer.is_valid(raise_exception=True)
        return Response(None, status=status.HTTP_202_ACCEPTED)

class LogoutView(APIView):
    """ view to logout a user """
    def post(self, request):
        logout(request)
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProfileView(RetrieveUpdateDestroyAPIView):
    """ view for the updating or deleting a user profile """
    queryset = models.UserProfile.objects.all()
    serializer_class = UpdateUserSerializer
    permission_classes = [UpdateOwnProfile]

    def get_object(self):
        return self.request.user
   
class UserProfileViewSet(viewsets.ModelViewSet):
    """ handles all CRUD operation on Profiles """
    serializer_class=UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=[UpdateOwnProfile]
    filter_backends=(filters.SearchFilter,)
    search_fields=(
        'username',
        'name',
        'email'
        )

class ResetPasswordView(UpdateAPIView):
    """ change the user password """
    queryset = models.UserProfile.objects.all()
    serializer_class = ResetPasswordSerializer
    permission_classes = [UpdateOwnProfile]

    def get_object(self):
        return self.request.user