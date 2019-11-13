from django.shortcuts import render
from django.http import HttpResponse


def home( request):
    return render ( request, 'choco/templates/index.html')

def cadastro_pacote (request):
    return render ( request, 'choco/templates/cadastro_pacote.html')
# Create your views here.
