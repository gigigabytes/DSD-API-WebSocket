from rest_framework import serializers
from .models import Livro, Usuario,Estante, Emprestimo
from django.contrib.auth.hashers import make_password, check_password

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

class EmprestimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emprestimo
        fields = '__all__'


class CadastroSerializer(serializers.ModelSerializer):
    senha2 = serializers.CharField(write_only = True)
    class Meta:
        model = Usuario
        fields = ('nome','senha','senha2')

    
    def validate(self, data):
        if data['senha'] != data['senha2']:
            raise serializers.ValidationError({"senha": "As senhas não coincidem."})
        return data

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])
        return Usuario.objects.create(**validated_data)
    
class LoginSerializer(serializers.Serializer):
    nome = serializers.CharField()
    senha = serializers.CharField(write_only = True)

    
