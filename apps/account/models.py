from ast import BinOp
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

#base model
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, editable=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __unicode__ (self) -> any:
        return self.name

#expanded model
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """represents a user profile in our database"""
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, null=True)
    last_name:  models.CharField(max_length=100, null=True)
    title = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=254, unique=True, editable=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    date_updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff: models.BooleanField(default=False)
    
    objects=UserProfileManager()
    
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """used to get a user fullname."""
        
        return (self.first_name + "" + self.last_name)
    def get_short_name(self):
        """used to get user first/short name"""    
        return self.first_name
    
    def __str__(self):
        """to convert the object to a string"""  
        return self.email
    #returning a field unique to the user


#userprofilemanager
class UserProfileManager:
    passA