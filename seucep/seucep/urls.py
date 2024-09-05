from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from core import views  # Certifique-se de importar as views do app core

# Configuração do Swagger
schema_view = get_schema_view(
   openapi.Info(
      title="API de Consulta de CEP",
      default_version='v1',
      description="Documentação da API para consulta de CEP usando Django e WebSocket",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="suporte@exemplo.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

# Rotas principais
urlpatterns = [
    path('admin/', admin.site.urls),  # Rota para o painel de administração
    path('', views.index, name='index'),  # Rota para a página inicial (index)

    # Incluir as rotas do app "core"
    path('api/', include('core.urls')),

    # Rota para a documentação Swagger e Redoc
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
