from django.urls import path
from . import views
from .views import buscar_cep

urlpatterns = [
    path('api/cep/<str:cep>/', views.cep_detail, name='cep-detail'),
    path('', buscar_cep, name='index'),

]
