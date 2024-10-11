from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)  # Asegura que la contraseña se guarde encriptada
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(username, email, password, **extra_fields)


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=20, default='a')
    telefono = models.CharField(max_length=10, blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    # Campos necesarios para el superusuario
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)  # Necesario para saber si es personal
    is_superuser = models.BooleanField(default=False)  # Superusuario

    USERNAME_FIELD = 'username'  # Se utilizará 'username' para autenticarse
    REQUIRED_FIELDS = ['email', 'nombre', 'telefono']  # Los campos requeridos al crear superusuarios

    objects = CustomUserManager()  # Asigna el manager personalizado

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Permiso para usuarios normales y superusuarios"""
        return self.is_superuser

    def has_module_perms(self, app_label):
        """Permiso para ver apps"""
        return self.is_superuser
