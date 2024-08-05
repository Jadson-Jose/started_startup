from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants

def cadastro(request):
    if request.method == "GET":
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if senha != confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não coincidem.')
            return redirect('/usuarios/cadastro')
        
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'A senha precisa ter pelo menos 6 dígitos.')
            return redirect('/usuarios/cadastro')

        users = User.objects.filter(username=username)
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com este usename.')
            return redirect('/usuarios/cadastro')

        user = User.objects.create_user(
            username=username,
            password=senha
        )

        return redirect('usuarios/logar')