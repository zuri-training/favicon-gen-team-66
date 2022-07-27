from django.db import models
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

from .manager import NewUserManager
from . import utils
class NewUser(AbstractUser):
    """ 
    For creating a custom user which depends on an email for login 
    """
    username = None
    slug = models.SlugField(unique = True, blank = True)
    email = models.EmailField(unique = True)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    
    object = NewUserManager()
    class Meta:
        """
        specifies how the user would be referenced or ordered by
        """
        verbose_name = 'User'
        ordering = ['email']
        
    def __str__(self):
        return self.email
    
    def new_slug(self):
        """
        concatenate the strings and create a slug
        if the slug exists already, run the finction again
        """
        created_slug = slugify(
            self.first_name + self.last_name + utils.generate_id()
            )
        while NewUser.objects.filter(slug = created_slug).exists():
            created_slug = slugify(
            self.first_name + self.last_name + utils.generate_id()
            )
        return created_slug
        
    def save(self, *args, **kwargs):
        # if user has no slug, create default slug 
        # from first name, last name and random id
        if not self.slug:
            # created_slug = slugify(
            #     self.first_name + self.last_name + utils.generate_id()
            #     )
            # while NewUser.objects.filter(slug = created_slug).exists():
            #     created_slug = slugify(
            #     self.first_name + self.last_name + utils.generate_id()
            #     )
                
            self.slug = self.new_slug()
        
        super().save(*args, **kwargs)
    