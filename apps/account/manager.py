from django.contrib.auth.base_user import BaseUserManager


class NewUserManager(BaseUserManager):
    """ 
    For managing the logic for custom user 
    """
    
    def create(self, email, password, **extra_fields):
        """ 
        Create extended user using email instead of username
        """
        if not email:
            raise ValueError('Enter an email')
        
        email = self.normalize_email(email)
        user = self.model(email = email, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    
    def create_superuser(self, email, password, **extra_fields):
        """ 
        Create extended superuser using custom model
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError("SuperUser must be a staff")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("SuperUser must be a SuperUser")
        return self.create(email, password, **extra_fields)