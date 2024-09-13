from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=115)
    autor = models.CharField(max_length=115)

class Usuario(models.Model):
    nome = models.CharField(max_length=115)

class Estante(models.Model):
    nome = models.CharField(max_length= 115)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro)
