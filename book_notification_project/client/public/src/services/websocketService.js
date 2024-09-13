export function connectWebSocket(userId) {
    const ws = new WebSocket(`ws://notification-service/ws/${userId}`);
  
    ws.onmessage = function(event) {
      console.log("Mensagem recebida: ", event.data);
    };
  }
  