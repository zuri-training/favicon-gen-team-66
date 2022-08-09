from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from . import models


User = get_user_model()
MINIMUM_LENGTH = 6

class UserSerializer(serializers.ModelSerializer):
    """ serializer for user information """
    class Meta:
        model = models.UserProfile
        fields = "__all__"

#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    """ serializer for registration of users """
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        min_length = MINIMUM_LENGTH,
        error_messages = {
            'minimum_length': f'Your password must be more than {MINIMUM_LENGTH} characters'
        }
    )
    password2 = serializers.CharField(
        write_only = True,
        min_length = MINIMUM_LENGTH,
        error_messages = {
            'minimum_length': f'Your password must be more than {MINIMUM_LENGTH} characters'
        }
    )
  
    class Meta:
        model = models.UserProfile
        fields = [
            'pk',
            'username', 
            'password', 
            'password2',
            'email', 
            'name'
            # 'first_name', 
            # 'last_name'
            ]
        extra_kwargs = {
            'email': {'required': True},
            'name': {'required': True}
            # 'first_name': {'required': True},
            # 'last_name': {'required': True}
        }
        
      # validate that both passwords match
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords do not match')
        return data
    
    # create user if validation is successful
    def create(self, validated_data):
        """ return output after creation """
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        
        # pass the validated password
        user.set_password(validated_data['password'])
        # save and return the created user
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    """ This is the serializer for logging in a user """
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, data):
        # Take username and password from request
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Authenticate the user
            user = authenticate(
                request=self.context.get('request'),
                username=username, 
                password=password
                )
            if not user:
                # Raise a ValidationError if user is not authenticated,
                msg = 'Access denied: invalid username or password.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Enter username or password'
            raise serializers.ValidationError(msg, code='authorization')
        data['user'] = user
        return data

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for user profile objects"""
    
    class Meta:
        model=models.UserProfile
        fields=('id','email', 'password', 'name', 'title', 'username', 'is_active')
        extra_kwargs={
            'password': {'write_only': True},
            'email': {'required': True},
            'name': {'required': True}
        }
        
        def create(self, validated_data):
            """create and returns new user"""
            user=models.UserProfile(
                  email = validated_data ['email'],
                  name = validated_data['name']
            )
            
            user.set_password(validated_data['password'])
            user.save()
            
            return user