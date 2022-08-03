from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator


User = get_user_model()
MINIMUM_LENGTH = 6


#Serializer to Get User Details using Django Token Authentication
class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
        'username', 
        'password', 
        'password2',
        'email', 
        'first_name', 
        'last_name'
        ]


#Serializer to Register User
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(
        write_only = True,
        min_length = MINIMUM_LENGTH,
        error_messages = {
            'minimum_length': f'Your password mist be more than {MINIMUM_LENGTH} characters'
        }
    )
    
    password2 = serializers.CharField(
        write_only = True,
        min_length = MINIMUM_LENGTH,
        error_messages = {
            'minimum_length': f'Your password mist be more than {MINIMUM_LENGTH} characters'
        }
    )
  
    class Meta:
        model = User
        fields = [
            'username', 
            'password', 
            'password2',
            'email', 
            'first_name', 
            'last_name'
            ]
        extra_kwargs = {
        'first_name': {'required': True},
        'last_name': {'required': True}
        }
        
      # validate that both passwords match
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('passwords do not match')
        return data
    
    # create user if validation is successful
    def create(self, validated_data):
        user = User.objects.create(
            email = validated_data['email'],
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
        )
        
        # pass the validated password
        user.set_password(validated_data['password'])
        
        # save the created user
        user.save()
        
        return user
