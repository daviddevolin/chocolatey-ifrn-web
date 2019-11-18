from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm
from .models import Pacote
def home( request):
    return render ( request, 'choco/templates/index.html')

def cadastro_pacote(request):
    if request.method == 'POST':
        #cadastrar pacote
        form = PostForm(request.POST)
        #pacote = form.save(commit=False)
        pacote = form.save()
        pacote.save()
        print(pacote.icon_URL)
    
    form = PostForm()
    pacote = Pacote.object.all()
    contexto = {'form': form,
                'pacotes': pacote}
    return render(request, 'choco/templates/cadastro_pacote.html',contexto )

def visualiza_pacote(request):
    pacote = Pacote.object.all()
    
    contexto = {'pacotes': pacote}
    
    return render(request, 'lista_pacotes.html', contexto)    

# Create your views here.

