
from .models import Postagem
from .models import Conteudo
from django.shortcuts import get_object_or_404, render
# todos/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def registrar_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            return redirect('paginas:home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})


def home(request):
    posts = Postagem.objects.all()
    # Recupere todos os conteúdos associados a todos os posts
    conteudos = Conteudo.objects.filter(postagem__in=posts)
    return render(request, 'paginas/home.html', {'posts': posts, 'conteudos': conteudos})

def postagem(request, postagem_id):
    postagem = Postagem.objects.get(pk=postagem_id)
    return render(request, 'paginas/postagem.html', {'postagem': postagem})

def conteudo(request, conteudo_id):
    conteudo = get_object_or_404(Conteudo, pk=conteudo_id)
    return render(request, 'paginas/conteudo.html', {'conteudo': conteudo})

def todos_conteudos(request, postagem_id):
    conteudos = Conteudo.objects.filter(postagem_id=postagem_id)
    return render(request, 'paginas/todos_conteudos.html', {'conteudos': conteudos})

def sobre(request):
    return render(request, 'paginas/sobre.html')

def contato(request):
    return render(request, 'paginas/contato.html')