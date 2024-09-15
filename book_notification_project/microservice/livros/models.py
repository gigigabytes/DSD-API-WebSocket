from django.db import models

# Create your models here.

class Livro(models.Model):
    titulo = models.CharField(max_length=115)
    autor = models.CharField(max_length=115)
    disponivel = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    nome = models.CharField(max_length=115)
    senha = models.CharField(max_length=115)

    def __str__(self):
        return self.nome

class Estante(models.Model):
    nome = models.CharField(max_length= 115)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livros = models.ManyToManyField(Livro)

    def __str__(self):
        return self.nome

class Emprestimo(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    dataemprestimo = models.DateTimeField(auto_now_add=True)
    datadevolucao = models.DateTimeField(null= True, blank=True)

    def __str__(self):
        return f"{self.livro.titulo} emprestado por {self.usuario.nome}"