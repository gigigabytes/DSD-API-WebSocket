import json
from channels.generic.websocket import AsyncWebsocketConsumer  # Usando AsyncWebsocketConsumer
from asgiref.sync import async_to_sync

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Aceita a conexão WebSocket
        await self.accept()

    async def notify_users(self, event):
        # Envia uma notificação para o usuário
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))

class BookNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Adiciona este canal ao grupo "livros"
        await self.channel_layer.group_add(
            "livros",
            self.channel_name
        )
        # Aceita a conexão WebSocket
        await self.accept()
        print("WebSocket conectado!")

    async def disconnect(self, close_code):
        # Remove o canal do grupo ao desconectar
        await self.channel_layer.group_discard(
            "livros",
            self.channel_name
        )
        print("WebSocket desconectado!")

    # Recebe mensagens do WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        print(f"Recebido do WebSocket: {message}")

        # Envia a mensagem de volta para o grupo "livros"
        await self.channel_layer.group_send(
            "livros",
            {
                'type': 'send_message',
                'message': message
            }
        )

    # Recebe mensagem do grupo
    async def send_message(self, event):
        message = event['message']

        # Envia a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))
        print(f"Mensagem enviada para o WebSocket: {message}")
