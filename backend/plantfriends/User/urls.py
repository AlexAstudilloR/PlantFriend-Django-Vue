from django.urls import path
from .views import RegisterUserView

urlpatterns = [
    path('registrarse/', RegisterUserView.as_view(), name='register'),
]
