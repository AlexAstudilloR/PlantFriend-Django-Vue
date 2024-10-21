from django.db import models
from plantfriends.Guides.models import Guides

class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name
# Create your models here.
class Plants(models.Model):
    nombre= models.CharField(max_length=20)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='plants/',null=True)
    guia= models.ForeignKey(Guides,on_delete= models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nombre, self.imagen
    