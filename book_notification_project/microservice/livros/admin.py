from django.contrib import admin
from .models import Livro, Estante,Usuario

# Register your models here.
admin.site.register(Livro)
admin.site.register(Estante)
admin.site.register(Usuario)