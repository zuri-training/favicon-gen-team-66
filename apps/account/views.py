from rest_framework.permissions import AllowAny, IsAdminUser
from django.contrib.auth import get_user_model
from .serializer import (
    UserSerializer, 
    RegisterSerializer,
    LoginSerializer
    )
from .permissions import (
    IsCreatorOrAdmin
)
from rest_framework.generics import (
    CreateAPIView, 
    ListAPIView, 
    RetrieveAPIView,
    ListAPIView
    )
from rest_framework.response import Response
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework import status

User = get_user_model()

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
    permission_classes = [IsAdminUser]
    """ Admin View to list of all users """
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all().order_by('date_joined')
    permission_classes = [IsAdminUser]
   