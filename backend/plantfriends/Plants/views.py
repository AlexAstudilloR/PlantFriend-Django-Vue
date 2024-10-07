from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Plants
from .serializers import PlantsSerializer

class PlantsListCreateView(generics.ListCreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer

# Vista para recuperar, actualizar y eliminar una planta específica
class PlantsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer

class PlantsCreateView(generics.CreateAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Obtiene los datos del request
        serializer.is_valid(raise_exception=True)  # Valida los datos
        self.perform_create(serializer)  # Crea la instancia
        return Response(serializer.data, status=status.HTTP_201_CREATED)  # Retorna una respuesta exitosa