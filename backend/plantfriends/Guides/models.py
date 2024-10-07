from django.db import models


class Guides(models.Model):
    descripcion=models.CharField(max_length=200)
    created_at= models.DateTimeField(auto_now_add=True)