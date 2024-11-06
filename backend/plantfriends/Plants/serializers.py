from rest_framework import serializers
from .models import Plants, Category
from plantfriends.Guides.models import Guides

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
from rest_framework import serializers
from .models import Plants, Category
from plantfriends.Guides.models import Guides

class PlantsSerializer(serializers.ModelSerializer):
    guia = serializers.PrimaryKeyRelatedField(queryset=Guides.objects.all())
    categoria = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    imagen = serializers.ImageField(use_url=True)  # Cambia a ImageField para manejar la carga de archivos

    class Meta:
        model = Plants
        fields = ['id', 'nombre', 'categoria', 'imagen', 'guia', 'nombre_cientifico','created_at']