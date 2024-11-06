from django.urls import path
from .views import ScanPlant


urlpatterns= [
    path('escanear/', ScanPlant,name='escanear')
]