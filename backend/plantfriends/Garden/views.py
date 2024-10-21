from rest_framework import generics
from plantfriends.Garden.models import Garden
from .serializer import GardenSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from plantfriends.Plants.models import Plants
# Listar el jardín del usuario autenticado
class UserGardenList(generics.ListAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Garden.objects.filter(usuario=user)

# Agregar una planta al jardín del usuario
class AddToGarden(generics.CreateAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        planta_id = self.kwargs['planta_id']  # Obtener la ID de la planta desde la URL
        planta = get_object_or_404(Plants, id=planta_id)  # Buscar la planta por su ID
        serializer.save(usuario=self.request.user, planta=planta)  # Guardar el jardín con la planta específica


# Eliminar una planta del jardín del usuario
class RemoveFromGarden(generics.DestroyAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        planta_id = self.kwargs['planta_id']  # Obtener la ID de la planta desde la URL
        return get_object_or_404(Garden, usuario=user, planta_id=planta_id)
