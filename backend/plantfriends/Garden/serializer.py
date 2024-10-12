from rest_framework import serializers
from plantfriends.Garden.models import Garden

class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = ['id','usuario', 'planta', 'guia', 'created_at']
