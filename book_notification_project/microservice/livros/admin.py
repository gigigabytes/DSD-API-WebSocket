from django.contrib import admin
from .models import Livro, Estante,Usuario, Emprestimo

# Register your models here.
admin.site.register(Livro)
admin.site.register(Estante)
admin.site.register(Usuario)
admin.site.register(Emprestimo)