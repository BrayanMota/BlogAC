from django.urls import path
from jogos import views

urlpatterns = [
    path('jogos', views.lista_jogos, name='lista_jogos'),
]
