from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserGardenList.as_view(), name='user-garden-list'),
    path('add/', views.AddToGarden.as_view(), name='add-to-garden'),
    path('remove/<int:planta_id>/', views.RemoveFromGarden.as_view(), name='remove-from-garden'),
]
