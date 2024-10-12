from django.db import models


class Guides(models.Model):
    descripcion=models.CharField()
    created_at= models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.descripcion  # Muestra el título en lugar del objeto en el administrador de Django