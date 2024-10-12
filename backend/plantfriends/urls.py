
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/plantas/',include('plantfriends.Plants.urls')),
    path('api/auth/guias/',include('plantfriends.Guides.urls')),
    path('api/auth/usuario/',include('plantfriends.User.urls')),
    path('api/auth/garden/', include('plantfriends.Garden.urls')),
]
