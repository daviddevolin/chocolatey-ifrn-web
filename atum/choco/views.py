from django.shortcuts import render
from django.http import HttpResponse


def home( request):
    return render ( request, 'choco/index.php')
# Create your views here.
