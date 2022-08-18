from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
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
            ]
        extra_kwargs = {
            'email': {'required': True},
            'name': {'required': True}
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
            name = validated_data['name']
        )
        
        # pass the validated password
        user.set_password(validated_data['password'])
        # save and return the created user
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    """ This is the serializer for logging in a user """
    username = serializers.CharField(
        label = "Username",
        write_only = True
    )
    password = serializers.CharField(
        label = "Password",
        # This will be used when the DRF browsable API is enabled
        style = {'input_type': 'password'},
        write_only = True
    )

    def validate(self, data):
        # Take username and password from request
        username = data.get('username')
        password = data.get('password')

        if username and password:
            # Authenticate the user
            user = authenticate(
                request = self.context.get('request'),
                username = username, 
                password = password
                )
            if not user:
                # Raise a ValidationError if user is not authenticated,
                msg = 'Access denied: invalid username or password.'
                raise serializers.ValidationError(msg, code = 'authorization')
        else:
            msg = 'Enter username or password'
            raise serializers.ValidationError(msg, code = 'authorization')
        data['user'] = user
        return data

class UpdatedLoginSerializer(serializers.Serializer):
    """ This is the serializer for logging in a user """
    username = serializers.CharField(
        label = "Username",
        write_only = True
    )
    password = serializers.CharField(
        label = "Password",
        style = {'input_type': 'password'},
        write_only = True
    )

    def validate(self, data):
        # Take username and password from request
        username = data.get('username')
        password = data.get('password')
        user = models.UserProfile.objects.filter(username = username).first()
        if user.check_password(password):
            return data

class UserProfileSerializer(serializers.ModelSerializer):
    """serializer for user profile objects"""
    class Meta:
        model = models.UserProfile
        fields = [
            'id',
            'email', 
            'password', 
            'name', 
            'title',
            'profile_pic',
            'username', 
            'is_active'
            ]
        extra_kwargs = {
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
        
class ResetPasswordSerializer(serializers.ModelSerializer):
    """ serializer for changing password"""
    password = serializers.CharField(
        write_only = True, 
        required = True, 
        validators = [validate_password])
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = [
            'old_password', 
            'password', 
            'password2'
        ]

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return data

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.set_password(validated_data['password'])
        instance.save()

        return instance

class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = [
            'username', 
            'name', 
            'title', 
            'email',
            'profile_pic'
        ]
        extra_kwargs = {
            'name': {'required': True},
        }

    def validate_email(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk = user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "This email is already in use."})
        return value

    def validate_username(self, value):
        user = self.context['request'].user
        if User.objects.exclude(pk = user.pk).filter(username=value).exists():
            raise serializers.ValidationError({"username": "This username is already in use."})
        return value

    def update(self, instance, validated_data):
        user = self.context['request'].user

        if user.pk != instance.pk:
            raise serializers.ValidationError({"authorize": "You dont have permission for this user."})

        instance.name = validated_data['name']
        instance.email = validated_data['email']
        instance.title = validated_data['title']
        instance.username = validated_data['username']
        instance.profile_pic = validated_data['profile_pic']

        instance.save()

        return instance