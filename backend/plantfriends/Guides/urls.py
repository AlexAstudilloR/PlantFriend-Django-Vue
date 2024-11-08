from django.urls import path
from .views import GuideShowView, GuideCreateView, GuideDetailView

urlpatterns = [
    path('', GuideShowView.as_view(), name='guide-show'),  # Para mostrar una guía específica
    path('crear/', GuideCreateView.as_view(), name='guide-create'),
    path('<int:id>/', GuideDetailView.as_view(), name='guide-detail'),      # Para crear una nueva guía (POST)
]
