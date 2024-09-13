// Função para conectar ao WebSocket
export function connectWebSocket(userId) {
    const ws = new WebSocket(`ws://localhost:8003/ws/${userId}`);
  
    ws.onopen = () => {
      console.log('WebSocket connection opened');
    };
  
    ws.onmessage = (event) => {
      console.log('Notification received:', event.data);
      alert(`Notification: ${event.data}`);
    };
  
    ws.onerror = (error) => {
      console.error('WebSocket error:', error);
    };
  
    ws.onclose = () => {
      console.log('WebSocket connection closed');
    };
  }
  