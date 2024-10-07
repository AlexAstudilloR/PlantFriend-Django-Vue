from rest_framework import serializers
from .models import Guides  # Importa tu modelo Guides

class GuidesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guides
        fields = ['id', 'descripcion', 'created_at']  # Incluye los campos que deseas serializar
