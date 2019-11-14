from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm

def home( request):
    return render ( request, 'choco/templates/index.html')

def cadastro_pacote(request):
    form = PostForm()
    return render(request, 'choco/templates/cadastro_pacote.html', {'form': form})

# Create your views here.
