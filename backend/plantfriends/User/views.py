from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.save()  # Llama a `create` en el serializer, que devuelve el usuario y los tokens
            return Response(user_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginUserView(TokenObtainPairView):
    permission_classes = [AllowAny] 
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        
        if response.status_code == 200:
            # Obtener el usuario autenticado
            user = CustomUser.objects.get(username=request.data['username'])
            
            # Añadir datos adicionales del usuario a la respuesta
            response.data['user'] = {
                'username': user.username,
                'imagen': user.imagen.url if user.imagen else None,
            }
        
        return response # Permitir que cualquiera pueda iniciar sesión
