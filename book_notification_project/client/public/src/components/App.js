import React, { useState } from 'react';
import { login } from './auth';
import { reserveBook, returnBook } from './books';
import { connectWebSocket } from './websocket';

function App() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = async () => {
    const result = await login(username, password);
    if (result) {
      connectWebSocket(username);  // Conectar ao WebSocket após login
    }
  };

  return (
    <div className="App">
      <h1>Book Reservation System</h1>

      <div>
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <button onClick={handleLogin}>Login</button>
      </div>

      <button onClick={() => reserveBook(1)}>Reserve Book 1</button>
      <button onClick={() => returnBook(1)}>Return Book 1</button>
    </div>
  );
}

export default App;
