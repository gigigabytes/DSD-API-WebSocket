const WebSocket = require('ws');

// Crie o servidor WebSocket na porta 8080
const wss = new WebSocket.Server({ port: 8080 });

// Função para obter a hora atual formatada
function getCurrentTime() {
  const now = new Date();
  return now.toLocaleTimeString('pt-BR', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
}

wss.on('connection', (ws) => {
  console.log('Novo cliente conectado');

  ws.on('message', (data) => {
    const parsedData = JSON.parse(data);  // Converte a mensagem recebida em objeto
    const { username, message } = parsedData;

    // Adiciona o horário à mensagem
    const time = getCurrentTime();
    const fullMessage = JSON.stringify({ username, message, time });

    // Enviar a mensagem para todos os clientes conectados
    wss.clients.forEach((client) => {
      if (client.readyState === WebSocket.OPEN) {
        client.send(fullMessage);
      }
    });
  });

  ws.on('close', () => {
    console.log('Cliente desconectado');
  });
});

console.log('Servidor WebSocket rodando na porta 8080');
