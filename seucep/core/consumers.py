import json
from channels.generic.websocket import WebsocketConsumer

class CEPConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        data = json.loads(text_data)
        cep = data['cep']
        # Resposta com o CEP
        response_message = f"Consulta para o CEP {cep} foi realizada!"
        self.send(text_data=json.dumps({
            'message': response_message
        }))
