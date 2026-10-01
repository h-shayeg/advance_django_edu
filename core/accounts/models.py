from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserManager(BaseUserManager):
    '''
    Custom user model manager where email is the unique identifiers for authentication instead of usernames.
    '''
    def create_user(self, email, password, **extra_filed):
        '''
        Create and save a User with the given email and password and extra data.
        '''
        if not email:
            raise ValueError(_("the Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_filed)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, email, password, **extra_filed):
        '''
        Create and save a SuperUser with the given email and password and extra data.
        '''
        extra_filed.setdefault('is_staff', True)
        extra_filed.setdefault('is_superuser', True)
        extra_filed.setdefault('is_active', True)

        if extra_filed.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_filed.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_filed)
        

class User(AbstractBaseUser, PermissionsMixin):
    '''
    this is a class to define users for the application
    '''

    email = models.EmailField(max_length=250, unique=True)
    is_superuser = models.BooleanField(default=False)
    username = models.CharField(max_length=250, unique=True)
    first_name = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # last_name = models.CharField(max_length=250)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # objects = BaseUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
    def __str__(self):
        return self.email