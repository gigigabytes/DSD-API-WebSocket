from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LivroViewSet, UsuarioViewSet, EstanteViewSet

router = DefaultRouter()
router.register(r'livros',LivroViewSet)
router.register(r'usuarios',UsuarioViewSet)
router.register(r'estantes',EstanteViewSet)

urlpatterns = [
    path('', include (router.urls))
]