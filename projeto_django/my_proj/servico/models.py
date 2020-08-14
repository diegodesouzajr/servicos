from django.db import models

# Create your models here.

from django.db import models
#from django.urls import reverse


class ServicoUm(models.Model):
    numero_par = models.IntegerField()

    def __str__(self):
        return self.numero_par


class ServicoDois(models.Model):
    numero_impar = models.IntegerField()

    def __str__(self):
        return self.numero_impar


class ServicoTres(models.Model):
    numero_multiplicado = models.IntegerField()

    def __str__(self):
        return self.numero_multiplicado


class ServicoQuatro(models.Model):
    numero_publicado = models.IntegerField()

    def __str__(self):
        return self.numero_publicado
