from django.db import models
from plantfriends.Plants.models import Plants
from plantfriends.User.models import CustomUser
from plantfriends.Guides.models import Guides


class Garden(models.Model):
    usuario = models.ForeignKey(CustomUser, on_delete=models.CASCADE) 
    planta = models.ForeignKey(Plants, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.usuario.nombre} - {self.planta.nombre}"

