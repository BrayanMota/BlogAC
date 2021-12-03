from django.urls import path
from jogos import views

urlpatterns = [
    path('', views.jogos, name='jogos'),
    path('serie_principal', views.serie_principal, name='serie_principal'),
]
