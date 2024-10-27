from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from plantfriends.Garden.serializer import GardenSerializer
from plantfriends.Garden.models import Garden
from plantfriends.Plants.models import Plants
from plantfriends.User.models import CustomUser
# Listar el jardín del usuario autenticado
class UserGardenList(generics.ListAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna el jardín del usuario autenticado
        return Garden.objects.filter(user=self.request.user)

class AddToGarden(generics.UpdateAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        garden, created = Garden.objects.get_or_create(user=request.user)
        plant_id = request.data.get("plant_id")
        
        try:
            plant = Plants.objects.get(id=plant_id)
            garden.plants.add(plant)
            return Response({"message": "Planta agregada al jardín."}, status=status.HTTP_200_OK)
        except Plants.DoesNotExist:
            return Response({"error": "Planta no encontrada."}, status=status.HTTP_404_NOT_FOUND)

class RemoveFromGarden(generics.UpdateAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        garden, created = Garden.objects.get_or_create(user=request.user)
        plant_id = kwargs.get("plant_id")

        try:
            plant = Plants.objects.get(id=plant_id)
            garden.plants.remove(plant)
            return Response({"message": "Planta eliminada del jardín."}, status=status.HTTP_200_OK)
        except Plants.DoesNotExist:
            return Response({"error": "Planta no encontrada."}, status=status.HTTP_404_NOT_FOUND)