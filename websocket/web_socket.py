from channels.generic.websocket import WebsocketConsumer
import json

class CEPConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        cep = data['cep']
        # Lógica para consultar o CEP
        self.send(text_data=json.dumps({
            'message': f'Informações do CEP {cep}'
        }))
