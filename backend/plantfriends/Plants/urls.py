from django.urls import path
from .views import (
    PlantsListCreateView, 
    PlantsDetailView, 
    PlantsSearchByNameView,
    PlantsSearchByScientificNameView,
    PlantsFilterByCategoryView, 
    CategoryCreateView, 
    CategoryListCreateView,
    PlantByGuideIdView
)

urlpatterns = [
    path('', PlantsListCreateView.as_view(), name='plants-list-show'),  # Listar y crear plantas
    path('<int:pk>/', PlantsDetailView.as_view(), name='plants-detail'),  # Recuperar, actualizar y eliminar plantas por ID
    path('crear/', PlantsListCreateView.as_view(), name='plants-list-create'),  # Crear plantas
    path('categoria/crear/', CategoryCreateView.as_view(), name='category-list-create'),  # Crear categoría
    path('categoria/', CategoryListCreateView.as_view(), name='category-list-show'),  # Listar categorías
    path('buscar/', PlantsSearchByNameView.as_view(), name='plants-search-by-name'),  # Buscar plantas por nombre
    path('filtrar/<str:category>/', PlantsFilterByCategoryView.as_view(), name='plants-filter-by-category'),
    path('buscar/cientifico/',PlantsSearchByScientificNameView.as_view(), name= 'search-by-scientific-name'),
    path('guia/<int:guia>/', PlantByGuideIdView.as_view(), name='plant-by-guide-id') # Filtrar plantas por categoría
]
