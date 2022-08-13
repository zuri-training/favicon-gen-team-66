from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.conf import settings
from . import utils
from . import models
from .serializer import (
    UserSerializer,
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer,
    SetNewPasswordSerializer,
    ResetPasswordEmailRequestSerializer,
)
from .permissions import (
    IsCreatorOrAdmin,
    UpdateOwnProfile,
)
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView
)
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework import status, generics, viewsets, filters
from django.utils.encoding import smart_str, force_str, force_bytes, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.http import request
from django.urls import reverse
import os
from django.shortcuts import redirect
from django.http import HttpResponsePermanentRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    UpdateAPIView
    )
from django.contrib.auth import logout
from django.conf import settings

from .permissions import UpdateOwnProfile
from .serializer import (
    RegisterSerializer,
    UserProfileSerializer,
    UpdatedLoginSerializer,
    ResetPasswordSerializer,
    UpdateUserSerializer
    )
from . import models


User = settings.AUTH_USER_MODEL

# Class based view to register user


class RegisterUserAPIView(CreateAPIView):
    """ View for user registration"""
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class LoginView(APIView):
    """ view for user login """
    permission_classes = [AllowAny]
    serializer_class = UpdatedLoginSerializer

    def post(self, request):
        serializer = LoginSerializer(
            data=self.request.data,
            context={'request': self.request}
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


class ProfileView(RetrieveAPIView):
    """ view for the user profile """
    serializer_class = UserSerializer
    permission_classes = [IsCreatorOrAdmin]

    def get_object(self):
        return self.request.user


class UserList(ListAPIView):
    """ Admin View to list of all users """
    User = models.UserProfile
    queryset = User.objects.all()
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('date_created')
    permission_classes = [IsAdminUser]


class UserProfileViewSet(viewsets.ModelViewSet):
    """handles all CRUD operation on Profiles"""

    serializer_class = UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username', 'name', 'email',)


class RequestPasswordResetEmail(generics.GenericAPIView):
    """Sends password reset link to User."""
    serializer_class = ResetPasswordEmailRequestSerializer
    model = models.UserProfile

    def post(self, request):
        # data={'request':request, 'data':request.data}
        serializer = self.serializer_class(data=request.data)

        email = force_bytes(request.data['email'])

        if get_user_model().objects.filter(email=email).exists():
            user = get_user_model().objects.get(email=email)
            uidb64 = urlsafe_base64_encode(user.id)
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relative_link = reverse(
                'password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            absolute_url = 'http://'+ current_site + relative_link
            email_body = 'Hello, \n Use link below to reset your password  \n' + absolute_url
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Reset your password'}
            utils.Util.send_mail(data)
        return Response({'success': 'check your email for a link to reset your password'}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPIView(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = get_user_model().objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'invalid token, please request a new one'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success': True, 'msg': 'valid credentials', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'invalid token, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)


class SetNewPasswordAPIView(generics.GenericAPIView):
    """Allows user to set a new password"""
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)
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

