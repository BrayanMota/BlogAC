from django.shortcuts import render
from .models import Jogos


def jogos(request):
    return render(request, 'jogos.html')


def serie_principal(request):
    jogos = Jogos.objects.all()
    
    lista_jogos = {
      'jogos': jogos
    }
    
    return render(request, 'serie_principal.html', lista_jogos)
