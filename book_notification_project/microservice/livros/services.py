from .models import Estante,Livro,Usuario, Emprestimo

from rest_framework.exceptions import ValidationError
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password


class LivroService:
    @staticmethod
    def getBooks():
        return Livro.objects.all()
    
    @staticmethod
    def addBook(data):
        if Livro.objects.filter(titulo = data['titulo']).exists():
            raise ValidationError("Livro já existe")
        livro = Livro.objects.create(**data)
        return livro

class EstanteService:
    @staticmethod
    def getShelfs():
        return Estante.objects.all()
    

class UsuarioService:
    @staticmethod
    def getUser():
        return Usuario.objects.all()

    def criar_usuario(nome,senha):
        senha_hash = make_password(senha)
        usuario = Usuario.objects.create(nome = nome, senha =senha_hash)
        return usuario
    

    def autenticar_usuario(nome, senha):
        try:
            usuario = Usuario.objects.get(nome = nome)
        except Usuario.DoesNotExist:
            return ("Usuário não encontrado")
        
        if check_password(senha, usuario.senha):
            return usuario
        return ("Error")
    
class EmprestimoService:
    @staticmethod
    def getEmprestimos():
        return Emprestimo.objects.all()

    def novo_emprestimo(livro_id, usuario):
        try:
            livro = Livro.objects.get(id = livro_id)
        except Livro.DoesNotExist:
            raise ValidationError("Livro não encontrado")
        if not livro.disponivel:
            raise ValidationError("Livro atualmente emprestado")
        
        emprestimo = Emprestimo.objects.create(livro = livro, usuario = usuario)
        livro.disponivel = False
        livro.save()

        return emprestimo
    

    def devolverLivro(livro_id):
        try:
            devolve = Emprestimo.objects.filter(livro_id =livro_id, return_datadevolucao__isnull = True).first()
        except Emprestimo.DoesNotExist:
            raise ValidationError ("Empréstimo não encontrado ou já devolvido")
        
        devolve.datadevolucao = timezone.now()
        devolve.save()

        devolve.livro.disponivel = True
        devolve.livro.save()

        return devolve