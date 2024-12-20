
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/plantas/',include('plantfriends.Plants.urls')),
    path('api/auth/guias/',include('plantfriends.Guides.urls')),
    path('api/auth/usuario/',include('plantfriends.User.urls')),
    path('api/auth/garden/', include('plantfriends.Garden.urls')),
    path('api/auth/scan/', include('plantfriends.Scan.urls'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)