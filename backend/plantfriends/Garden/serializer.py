
from rest_framework import serializers
from plantfriends.Garden.models import Garden
from plantfriends.Plants.models import Plants

class GardenSerializer(serializers.ModelSerializer):
    plants = serializers.PrimaryKeyRelatedField(queryset=Plants.objects.all(), many=True)

    class Meta:
        model = Garden
        fields = ['id', 'user', 'plants']
        read_only_fields = ['user']

    def create(self, validated_data):
        plants = validated_data.pop('plants', [])
        garden = Garden.objects.create(**validated_data)
        garden.plants.set(plants)
        return garden

    def update(self, instance, validated_data):
        plants = validated_data.pop('plants', None)
        if plants is not None:
            instance.plants.set(plants)
        return super().update(instance, validated_data)