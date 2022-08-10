from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from django.conf import settings
from . import models
from .serializer import (
    UserSerializer, 
    RegisterSerializer,
    LoginSerializer,
    UserProfileSerializer
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
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(
            data=self.request.data, 
            context={ 'request': self.request }
            )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
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
    User=models.UserProfile
    queryset = User.objects.all()
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by('date_created')
    permission_classes = [IsAdminUser]

   
class UserProfileViewSet(viewsets.ModelViewSet):
    """handles all CRUD operation on Profiles"""
    
    serializer_class=UserProfileSerializer
    queryset=models.UserProfile.objects.all()
    authentication_classes=(TokenAuthentication,)
    permission_classes=(UpdateOwnProfile,)
    filter_backends=(filters.SearchFilter,)
    search_fields=('username','name','email',)
    