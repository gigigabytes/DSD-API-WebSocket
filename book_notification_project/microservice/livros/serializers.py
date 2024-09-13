from rest_framework import serializers
from .models import Livro, Usuario,Estante

class LivroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Livro
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta :
        model = Usuario
        fields = '__all__'

class EstanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estante
        fields = '__all__'