import { getToken } from './auth';

// Função para reservar um livro
export async function reserveBook(bookId) {
  const token = getToken();

  try {
    const response = await fetch(`http://localhost:8002/reserve/${bookId}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error('Reservation failed');
    }

    const data = await response.json();
    console.log('Book reserved:', data);
  } catch (error) {
    console.error('Error during reservation:', error);
  }
}

// Função para devolver um livro
export async function returnBook(bookId) {
  const token = getToken();

  try {
    const response = await fetch(`http://localhost:8002/return/${bookId}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json'
      }
    });

    if (!response.ok) {
      throw new Error('Return failed');
    }

    const data = await response.json();
    console.log('Book returned:', data);
  } catch (error) {
    console.error('Error during return:', error);
  }
}
