from django.db import models

class Candidato(models.Model):
    imgPol = models.CharField(max_length=600)
    imgPart = models.CharField(max_length=600)
    imgUF = models.CharField(max_length=600)    
    siglaPart = models.CharField(max_length=10)
    nomeCand = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    twitter = models.CharField(max_length=200)

    def __str__(self):
        return self.nomeCand + " " + self.siglaPart

