// auth.js
export async function login(username, password) {
    try {
      const response = await fetch('http://localhost:8001/token', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams({
          'username': username,
          'password': password
        })
      });
  
      if (!response.ok) {
        throw new Error('Login failed');
      }
  
      const data = await response.json();
      
      // Salvando o token JWT no localStorage
      localStorage.setItem('token', data.access_token);
      return data;
    } catch (error) {
      console.error('Error during login:', error);
      return null;
    }
  }
  
  // Função para pegar o token JWT do localStorage
  export function getToken() {
    return localStorage.getItem('token');
  }
  