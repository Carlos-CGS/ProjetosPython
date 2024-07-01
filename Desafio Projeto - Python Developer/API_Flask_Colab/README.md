# Desafio Código DIO
# API Flask no Google Colab 

Este é um exemplo de como configurar uma API Flask no Google Colab que consome um arquivo JSON simples e exibe os dados em uma página web.

## Instalação
- Para executar este código, você precisa instalar o Flask e o ngrok no ambiente do Google Colab. Você pode fazer isso executando o seguinte comando:

- !pip install flask flask-ngrok

### Funcionamento
- Inicialização: O código inicia uma aplicação Flask e utiliza o flask-ngrok para criar uma URL pública que pode ser acessada.

### Rotas:
- ( /index  ):Exibe os dados JSON.
- (  /  ): Exibe a mensagem "Hello World!".

### Execução
- Após executar o código no Google Colab, você verá uma saída com a URL pública criada pelo ngrok. 
- Acesse essa URL seguida por /index para ver os dados JSON e / para ver a mensagem "Hello World!".