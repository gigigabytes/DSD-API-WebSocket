from rest_framework import viewsets
from .models import Livro, Usuario,Estante
from .serializers import LivroSerializer, UsuarioSerializer, EstanteSerializer


class LivroViewSet(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class EstanteViewSet(viewsets.ModelViewSet):
    queryset = Estante.objects.all()
    serializer_class = EstanteSerializer