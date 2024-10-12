from rest_framework import serializers
from .models import Plants,Category
from plantfriends.Guides.models import Guides

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields= ['id','name']

class PlantsSerializer(serializers.ModelSerializer):
    guia=serializers.PrimaryKeyRelatedField(queryset=Guides.objects.all())
    categoria=serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model = Plants
        fields = ['id', 'nombre', 'categoria','imagen', 'guia', 'created_at']  
