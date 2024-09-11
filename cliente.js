document.getElementById('searchInput').addEventListener('input', async function() {
    const query = this.value;
    
    if (query.length < 3) {
        // Não pesquisar se a consulta for muito curta
        return;
    }

    try {
        const response = await fetch(`https://www.googleapis.com/books/v1/volumes?q=${encodeURIComponent(query)}`);
        const data = await response.json();

        const resultsList = document.getElementById('resultsList');
        resultsList.innerHTML = ''; // Limpar resultados anteriores

        // Supondo que data.items seja um array de resultados
        data.items
            .slice(0, 10) // Seleciona os primeiros 10 itens
            .forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = item.volumeInfo.title; // Ajusta para o campo correto
                resultsList.appendChild(listItem);
            });

    } catch (error) {
        console.error('Erro ao buscar dados:', error);
    }
});
