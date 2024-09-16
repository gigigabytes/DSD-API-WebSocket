from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet,UsuarioViewSet,EstanteViewSet,EmprestimoViewSet
from .views import LoginView, CadastroView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = DefaultRouter()
router.register(r'livros',LivroViewSet)
router.register(r'usuarios',UsuarioViewSet)
router.register(r'estantes',EstanteViewSet)
router.register(r'emprestimos',EmprestimoViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title = "API Biblioteca",
        default_version='v1',
        description="Documentação da API de Empréstimo de Livros",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="suporte@exemplo.com"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('register/', CadastroView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Remova o prefixo 'api/'
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Remova o prefixo 'api/'
]
