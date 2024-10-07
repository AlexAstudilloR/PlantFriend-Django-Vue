from rest_framework import serializers
from .models import Plants
from plantfriends.Guides.models import Guides

class PlantsSerializer(serializers.ModelSerializer):
    guia=serializers.PrimaryKeyRelatedField(queryset=Guides.objects.all())
    class Meta:
        model = Plants
        fields = ['id', 'nombre', 'categoria', 'guia', 'created_at']  # Incluye los campos que deseas serializar
