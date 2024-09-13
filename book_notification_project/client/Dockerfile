# Usando uma imagem base do Node.js
FROM node:16-alpine

# Criando o diretório de trabalho no contêiner
WORKDIR /app

# Copiando o arquivo package.json e instalando as dependências
COPY package.json ./
RUN npm install

# Copiando o restante do código para o contêiner
COPY . .

# Construindo o projeto React
RUN npm run build

# Expondo a porta 3000 para o servidor de desenvolvimento
EXPOSE 3000

# Comando para rodar o servidor de desenvolvimento
CMD ["npm", "start"]
