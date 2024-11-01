from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserSerializer(serializers.ModelSerializer):
    imagen = serializers.ImageField(use_url=True,required =False) 
    class Meta:
        model = CustomUser
        fields = ['username', 'nombre', 'password', 'telefono', 'email', 'imagen','created_at']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        try:
            user = CustomUser(
                username=validated_data['username'],  # Asegúrate de que 'username' esté en validated_data
                email=validated_data['email'],
                nombre=validated_data['nombre'],
                telefono=validated_data['telefono'],
                imagen=validated_data['imagen']
            )
            user.set_password(validated_data['password'])  # Almacena la contraseña de forma segura
            user.save()

            # Genera el token JWT
            refresh = RefreshToken.for_user(user)
            
            # Serializa el usuario antes de devolverlo
            user_data = CustomUserSerializer(user).data  # Serializamos el usuario aquí

            return {
                'user': user_data,  # Devolvemos los datos del usuario serializados
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        except KeyError as e:
            raise serializers.ValidationError({str(e): 'Este campo es obligatorio.'})