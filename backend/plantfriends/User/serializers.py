from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'nombre', 'telefono', 'password', 'created_at']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Crear el usuario con el método adecuado para manejar la contraseña
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            nombre=validated_data['nombre'],
            telefono=validated_data['telefono']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        # Actualizar el usuario manejando la contraseña de forma segura
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
