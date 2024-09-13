const token = localStorage.getItem('token');

export async function reserveBook(bookId) {
  const response = await fetch(`http://book-service/reserve/${bookId}`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  const data = await response.json();
  console.log(data);
}

export async function returnBook(bookId) {
  const response = await fetch(`http://book-service/return/${bookId}`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    }
  });
  const data = await response.json();
  console.log(data);
}
