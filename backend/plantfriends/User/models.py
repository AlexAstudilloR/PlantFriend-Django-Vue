from django.contrib.auth.models import AbstractBaseUser
from django.db import models

class CustomUser(AbstractBaseUser):
    username= models.CharField(max_length=10,unique=True)
    email=models.EmailField()
    nombre=models.CharField(max_length=20,default='a')
    password=models.CharField()
    telefono = models.CharField(max_length=10, blank=True,default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD= 'username'
    REQUIRED_FIELDS= ['email','password','nombre',"telefono"]
    def __str__(self):
        return self.username
