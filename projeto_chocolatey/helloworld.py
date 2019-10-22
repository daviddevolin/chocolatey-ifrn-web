from django.conf.urls import url
from django.http import HttpResponse
from django.shortcuts import render

SECRET_KEY = 'helloworld'
DEBUG = True
ROOT_URLCONF = __name__
TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'APP_DIRS': True,
		'DIRS': 'C:\\Users\\01756847401\\Documents\\chocolatey-ifrn-web\\projeto_chocolatey\\templates'
	}
]

def hello_world(request):
	return render(request, 'templates/index.html')


urlpatterns = [
	url(r'^$', hello_world)

]

