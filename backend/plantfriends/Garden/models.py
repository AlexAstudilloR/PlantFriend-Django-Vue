from django.db import models
from plantfriends.Plants.models import Plants
from plantfriends.User.models import CustomUser
from plantfriends.Guides.models import Guides



class Garden(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='garden', default='')
    plants = models.ManyToManyField(Plants, related_name='gardens', blank=True)

    def __str__(self):
        return f"Jardín de {self.user.username}"