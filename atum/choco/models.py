from django.db import models

class pacote (models.Model):
    #arquivonuspec
    id_do_pacote = models.CharField( max_length=50)
    title = models.CharField( max_length=50)
    version = models.IntegerField()
    authors = models.CharField( max_length=50)
    owners = models.CharField( max_length=50)
    summary = models.CharField( max_length=50)
    project_URL= models.CharField( max_length=50)
    icon_URL = models.CharField( max_length=50)
    description = models.TextField()
    require_license_acceptance = models.BooleanField()
    dependencia = models.CharField( max_length=50)
    #arquivo chocolatey install
    installer_type = models.CharField( max_length=3)
    unattended_arguments = models.CharField( max_length=50)
    URL = models.CharField( max_length=50)
    URL_64 = models.CharField( max_length=50)

    
    
# Create your models here.
