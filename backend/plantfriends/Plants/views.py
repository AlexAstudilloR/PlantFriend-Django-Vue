import django_filters
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from .models import Plants,Category
from .serializers import PlantsSerializer, CategorySerializer
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

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
    
class CategoryCreateView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)  # Obtiene los datos del request
        serializer.is_valid(raise_exception=True)  # Valida los datos
        self.perform_create(serializer)  # Crea la instancia
        return Response(serializer.data, status=status.HTTP_201_CREATED)  
    
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
class PlantsSearchByNameView(generics.ListAPIView):
    queryset = Plants.objects.all()
    serializer_class = PlantsSerializer
    filter_backends = [filters.SearchFilter]  # Habilitamos la búsqueda
    search_fields = ['nombre']  # Campo de búsqueda: 'name'

class PlantsFilterByCategoryView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, category):
        if category == "all":
            plants = Plants.objects.all()
        else:
            plants = Plants.objects.filter(categoria__name=category)  # Ajusta el filtro según el campo de categoría en tu modelo

        serializer = PlantsSerializer(plants, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)