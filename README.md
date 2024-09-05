# Tarefa: Implementação de Transmissão de Dados com WebSocket

## Meta
Implementar, por meio de um estudo de caso, a transmissão de dados com WebSocket.

## Regras do API Gateway
- Desenvolver ao menos um API Gateway.
- Implementar o conceito de HATEOAS no Gateway.
- Criar a documentação de API para o Gateway (ex.: SOAP UI, Swagger, etc.).
- Implementar ou utilizar ao menos 2 APIs para simular a arquitetura interna de um sistema.
- Desenvolver um Cliente Web para acessar o Gateway.
 
## Regras do WebSocket
- Criar o servidor:
  - Classe que fornece um endpoint WebSocket e gerencia o ciclo de vida.
- Criar o cliente:
  - Instanciar o objeto WebSocket em um navegador Web e gerenciar o ciclo de vida.

## Arquivos do Projeto

### 1. `api.py`
Contém o código do API Gateway implementado com FastAPI. Inclui endpoints para interagir com microsserviços e aplicar autenticação JWT.

### 2. `websocket.py`
Implementa o servidor WebSocket, incluindo a autenticação JWT e o gerenciamento de mensagens.

### 3. `cliente.html`
Página HTML que funciona como cliente WebSocket, permitindo enviar mensagens e receber respostas do servidor WebSocket.

### 4. `generate_secret_key.py`
Script para gerar uma chave secreta para JWT. Execute este script para gerar uma chave segura e substitua a chave no arquivo `api.py` e `websocket.py`.

## Rodando o Projeto

1. **Instale as dependências**:
   - Certifique-se de que o Python está instalado.
   - Crie e ative um ambiente virtual:
     ```bash
     python -m venv venv
     source venv/bin/activate  # Em Windows: venv\Scripts\activate
     ```
   - Instale as bibliotecas necessárias:
     ```bash
     pip install fastapi uvicorn pyjwt requests
     ```

2. **Inicie o servidor API Gateway**:
   ```bash
   uvicorn api:app --host 0.0.0.0 --port 8001
