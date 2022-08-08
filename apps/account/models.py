from ast import BinOp
from tkinter import CASCADE
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

#base model
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, editable=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__ (self) -> any:
        return self.name


#userprofilemanager
class UserProfileManager(BaseUserManager):
    """helps django work with our docstring"""
    def create_user(self, email, name, password):
        """creates a new profile object."""
        
        if not email:
            raise ValueError('Users must have an email address')
        
        email=self.normalize_email(email) #normalizes the email address
        user = self.model(email=email, name= name)
        
        user.set_password(password)
        user.save(using=self._db)
        
        return user

    def create_superuser(self, email, name, password):
        """create and saves a new user with the given details"""
        
        user=self.create_user(email, name, password)
        user.is_superuser=True
        user.is_staff=True
        
        user.save(using=self._db)
        return user
#expanded model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """represents a user profile in our database"""
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=100, null=True)
    name=models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, unique=True, editable=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False)
    
    objects=UserProfileManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get a user fullname."""
        
        return self.name
    def get_short_name(self):
        """used to get user first/short name"""    
        return self.username
    
    def __str__(self):
        """to convert the object to a string"""  
        return self.email
    #returning a field unique to the user


