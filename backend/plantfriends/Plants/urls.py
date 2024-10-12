from django.urls import path
from .views import *

urlpatterns = [
    path('', PlantsListCreateView.as_view(), name='plants-list-show'),  # Listar y crear
    path('<int:pk>/', PlantsDetailView.as_view(), name='plants-detail'),  
    path('crear/', PlantsListCreateView.as_view(), name='plants-list-create'),
    path('categoria/crear/',CategoryCreateView.as_view(),name= 'category-list-create'),
    path('categoria/',CategoryListCreateView.as_view(),name= 'category-list-show'),
]
