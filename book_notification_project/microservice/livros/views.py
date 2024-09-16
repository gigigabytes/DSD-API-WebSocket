from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Livro, Usuario,Estante, Emprestimo
from .serializers import LivroSerializer, UsuarioSerializer, EstanteSerializer, EmprestimoSerializer, CadastroSerializer, LoginSerializer
from .services import LivroService, EstanteService, UsuarioService, EmprestimoService
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.permissions import IsAuthenticated


class LivroViewSet(viewsets.ModelViewSet):
   queryset = LivroService.getBooks()
   serializer_class = LivroSerializer

   def addLivro(self,serializer):
       LivroService.addBook(serializer.validated_data)

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = UsuarioService.getUser()
    serializer_class = UsuarioSerializer

    def addUsuario(self, serializer):
        UsuarioService.addUser(serializer.validated_data)

class EstanteViewSet(viewsets.ModelViewSet):
    queryset = EstanteService.getShelfs()
    serializer_class = EstanteSerializer

class EmprestimoViewSet(viewsets.ModelViewSet):
    queryset = EmprestimoService.getEmprestimos()
    serializer_class = EmprestimoSerializer

    def create(self, request):
            livro_id = request.data.get('livro')
            usuario = request.user
            emprestimo = EmprestimoService.novo_emprestimo(livro_id, usuario)
            serializer = EmprestimoSerializer(emprestimo)

            # Enviar notificação via WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                'notifications',  # Nome do grupo do WebSocket
                {
                    'type': 'notify_users',
                    'message': f'{usuario.username} fez um empréstimo do livro {emprestimo.livro.titulo}.'
                }
            )

            return Response(serializer.data, status= status.HTTP_201_CREATED)

    def devolve(self, request, pk=None):
        emprestimo = EmprestimoService.devolverLivro(pk)
        serializer = EmprestimoSerializer(emprestimo)

        # Enviar notificação via WebSocket
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "book_notifications", {
                "type": "notify_group",
                "message": f"O livro '{emprestimo.livro.titulo}' foi devolvido!"
            }
        )

        return Response(serializer.data)

class CadastroView(APIView):
    def post(self, request,*args,**kwargs):
        serializer = CadastroSerializer(data= request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            senha = serializer.validated_data['senha']
            UsuarioService.criar_usuario(nome,senha)
            return Response ({'message': 'Usuario cadastrado com sucesso'}, status= status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            senha = serializer.validated_data['senha']
            usuario = UsuarioService.autenticar_usuario(nome,senha)

            if usuario:
                refresh = RefreshToken.for_user(usuario)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Credenciais Inválidas'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)