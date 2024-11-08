from rest_framework import generics
from .models import Guides
from .serializers import GuidesSerializer
from rest_framework.response import Response
from rest_framework import status

class GuideShowView(generics.ListCreateAPIView):
    queryset = Guides.objects.all()  # Obtiene todos los objetos Guides
    serializer_class = GuidesSerializer  # Usa el serializador definido

class GuideCreateView(generics.CreateAPIView):
    queryset = Guides.objects.all()  # Obtiene todos los objetos Guides
    serializer_class = GuidesSerializer  # Usa el serializador definido
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Obtiene los datos del request
        serializer.is_valid(raise_exception=True)  # Valida los datos
        self.perform_create(serializer)  # Crea la instancia
        return Response(serializer.data, status=status.HTTP_201_CREATED) 
    
class GuideDetailView(generics.RetrieveAPIView):
    queryset = Guides.objects.all()  # Obtiene todas las guías
    serializer_class = GuidesSerializer  # Usa el serializador de guías
    lookup_field = 'id'  # Busca por el campo 'id' en el modelo Guides