from django.urls import path
from .consumers import CEPConsumer

websocket_urlpatterns = [
    path('ws/cep/', CEPConsumer.as_asgi()),
]
