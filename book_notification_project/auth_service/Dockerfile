# Usando uma imagem base do Python
FROM python:3.10-slim

# Criando o diretório de trabalho no contêiner
WORKDIR /app

# Copiando os arquivos requirements.txt e instalando as dependências
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiando o restante do código para o contêiner
COPY . .

# Expondo a porta 8001 para o serviço de autenticação
EXPOSE 8001

# Comando para rodar o serviço de autenticação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8001"]
