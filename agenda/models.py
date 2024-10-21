from django.db import models


class Solucao(models.Model):
    time = models.TimeField()
    timeid = models.CharField(max_length=100,blank=True)
    estado = models.CharField(max_length=100,blank=True)
    capacidade = models.CharField(max_length=100,blank=True)
    acoes = models.CharField(max_length=100,blank=True)
    otima = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return f"Exames e consultas de "