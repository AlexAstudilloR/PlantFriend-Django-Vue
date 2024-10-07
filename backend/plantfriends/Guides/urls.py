from django.urls import path
from .views import GuideShowView, GuideCreateView

urlpatterns = [
    path('', GuideShowView.as_view(), name='guide-show'),  # Para mostrar una guía específica
    path('crear/', GuideCreateView.as_view(), name='guide-create'),      # Para crear una nueva guía (POST)
]
