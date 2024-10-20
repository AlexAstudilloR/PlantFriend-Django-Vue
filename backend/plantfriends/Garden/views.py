from rest_framework import generics
from plantfriends.Garden.models import Garden
from .serializer import GardenSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

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
        serializer.save(usuario=self.request.user)
    

# Eliminar una planta del jardín del usuario
class RemoveFromGarden(generics.DestroyAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user = self.request.user
        planta_id = self.kwargs['planta_id']  # Obtener la ID de la planta desde la URL
        return get_object_or_404(Garden, usuario=user, planta_id=planta_id)
