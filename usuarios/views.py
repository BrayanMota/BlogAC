from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        senha = request.POST['senha']
        
        if email == '' or senha == '':
            print('Email e senha vazias')
            return redirect('login')
        if User.objects.filter(email=email).exists():
            nome = User.objects.filter(email=email).values_list('username', flat=True).get()
            usuario = auth.authenticate(request, username=nome, password=senha)
            if usuario is not None:
                auth.login(request, usuario)
                print('Login realizado com sucesso')
        return redirect('home')
        
    return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return render(request, 'home.html')


def perfil(request):
    if request.user.is_authenticated:
        return render(request, 'perfil.html')
    return redirect('home')
