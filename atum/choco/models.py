from django.db import models

class pacotes (models.Model):
    nome = models.CharField( max_length=50)
    title = models.CharField( max_length=50)
    version = models.IntegerField()
    authors = models.CharField( max_length=50)
    owners = models.CharField( max_length=50)
    summary = models.CharField( max_length=50)
    project_URL= models.CharField( max_length=50)
    icon_URL = models.CharField( max_length=50)
    description = models.TextField()
    require_license_acceptance = models.BooleanField()
    dependêcia = models.CharField( max_length=50)
    
# Create your models here.
