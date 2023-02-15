from django.db import models

class Filme(models.Model):    
    foto = models.CharField(max_length=100, null=False, blank=False)
    nome = models.CharField(max_length=100, null=False, blank=False)
    ano = models.IntegerField(null=False, blank=False)
    recomendacao = models.IntegerField(null=False, blank=False)
    estudio = models.CharField(max_length=100, null=False, blank=False)
    sinopse = models.TextField(max_length=500, null=False, blank=False)

    def __str__(self):
        return f"{self.nome}"
    

