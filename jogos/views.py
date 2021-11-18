from django.shortcuts import render
from .models import Jogos

def lista_jogos(request):
    jogos = Jogos.objects.all()
    
    lista_jogos = {
      'jogos': jogos
    }
    
    return render(request, 'lista_jogos.html', lista_jogos)
