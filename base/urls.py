from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('usuarios.urls')),
    path('jogos/', include('jogos.urls')),
    path('noticias/', include('noticias.urls')),
    path('admin/', admin.site.urls),
]
