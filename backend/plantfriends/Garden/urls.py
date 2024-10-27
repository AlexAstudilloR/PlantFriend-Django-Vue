from django.urls import path
from .views import UserGardenList, AddToGarden, RemoveFromGarden

urlpatterns = [
    path('', UserGardenList.as_view(), name='user-garden-list'),  # Lista el jardín del usuario autenticado
    path('add/', AddToGarden.as_view(), name='add-to-garden'),    # Agrega una planta al jardín del usuario autenticado
    path('remove/<int:plant_id>/', RemoveFromGarden.as_view(), name='remove-from-garden'),  # Elimina una planta del jardín del usuario autenticado
]
