from rest_framework import serializers
from plantfriends.Garden.models import Garden
from plantfriends.Plants.models import Plants
from plantfriends.User.models import CustomUser

class GardenSerializer(serializers.ModelSerializer):
    planta= serializers.StringRelatedField()
    usuario= serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all())

    class Meta:
        model = Garden
        
        fields = ['id','usuario', 'planta', 'created_at']
