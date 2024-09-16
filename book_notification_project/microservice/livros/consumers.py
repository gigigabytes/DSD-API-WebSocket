# livros/consumers.py
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.generic.websocket import WebsocketConsumer

class NotificationConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def notify_users(self, event):
        # Envia a notificação para todos os usuários conectados
        self.send(text_data=json.dumps({
            'message': event['message']
        }))

class BookNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']

        # Enviar a mensagem para o WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    async def notify_group(self, event):
        # Enviar notificação para o grupo
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
