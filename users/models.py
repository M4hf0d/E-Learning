from django.db import models
from django.contrib.auth.models import AbstractUser


import time
from datetime import datetime


from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(email, password, **extra_fields)



class User(AbstractUser):
    name = models.CharField(max_length=100, null = True)
    email = models.EmailField(unique=True, null = True)
    bio = models.TextField(null = True, blank = True)
    teacher = models.BooleanField(default=False, null = True)
    avatar = models.ImageField( upload_to='./Profile_images/',default="./Profile_images/def.jpg", null = True,blank=True)

    USERNAME_FIELD = 'email'   # Auth with EmailField
    REQUIRED_FIELDS=['username']

    objects = CustomUserManager()