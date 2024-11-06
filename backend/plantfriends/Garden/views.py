from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from plantfriends.Garden.serializer import GardenSerializer
from plantfriends.Garden.models import Garden
from plantfriends.Plants.models import Plants

# Listar el jardín del usuario autenticado
class UserGardenList(generics.ListAPIView):
    serializer_class = GardenSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Retorna el jardín del usuario autenticado
        return Garden.objects.filter(user=self.request.user)

# Agregar una planta al jardín
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from plantfriends.Garden.models import Garden
from plantfriends.Plants.models import Plants

class AddToGarden(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        garden, created = Garden.objects.get_or_create(user=request.user)
        plant_id = request.data.get("plant_id")

        if not plant_id:
            return Response({"error": "ID de planta no proporcionado."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            plant = Plants.objects.get(id=plant_id)
            garden.plants.add(plant)  # Agregar la planta al ManyToManyField
            garden.save()  # Guardar cambios en la base de datos
            return Response({"message": "Planta agregada al jardín."}, status=status.HTTP_200_OK)
        except Plants.DoesNotExist:
            return Response({"error": "Planta no encontrada."}, status=status.HTTP_404_NOT_FOUND)

# Eliminar una planta del jardín
class RemoveFromGarden(APIView):
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
