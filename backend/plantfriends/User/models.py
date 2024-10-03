from django.db import models

# Create your models here.
class User(models.Model):
    nombre= models.CharField(max_length=20)
    telefono= models.CharField(max_length=10)
    email= models.EmailField(unique=True)
    password= models.CharField()
    created_at=models.DateTimeField(auto_now_add=True)