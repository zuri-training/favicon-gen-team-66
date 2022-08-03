from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializer import (
    UserSerializer, 
    RegisterSerializer
    )


User = get_user_model()
# Class based view to Get User Details using Token Authentication
class UserDetailAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    def get(self,request,*args,**kwargs):
        user = User.objects.get(id=request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
