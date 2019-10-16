from django.conf.urls import url
from django.http import HttpResponse

SECRET_KEY = 'helloworld'
DEBUG = True
ROOT_URLCONF = __name__

def hello_world(request):
	return HttpResponse('Hello world!!!')


urlpatterns = [
	url(r'^$', hello_world)

]

