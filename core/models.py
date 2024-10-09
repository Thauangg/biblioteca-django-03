from django.db import models
from django.utils import timezone  # Importe isso no topo do arquivo
from datetime import datetime

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Autor(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey('Autor', on_delete=models.CASCADE)
    categoria = models.ForeignKey('Categoria', on_delete=models.SET_NULL, null=True)
    ano_publicacao = models.IntegerField()  # Este campo é obrigatório
    publicado_em = models.DateField(default=timezone.now)  # Modificado esta linha
    isbn = models.CharField(max_length=13, null=True, blank=True)

    def __str__(self):
        return self.titulo

    def save(self, *args, **kwargs):
        if isinstance(self.publicado_em, datetime):
            self.publicado_em = self.publicado_em.date()
        super().save(*args, **kwargs)