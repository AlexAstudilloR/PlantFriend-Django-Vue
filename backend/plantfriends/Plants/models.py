from django.db import models
from plantfriends.Guides.models import Guides
# Create your models here.
class Plants(models.Model):
    nombre= models.CharField(max_length=20)
    categoria= models.CharField(max_length=20)
    guia= models.ForeignKey(Guides,on_delete= models.CASCADE)
    created_at= models.DateTimeField(auto_now_add=True)
    