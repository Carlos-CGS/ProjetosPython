# Exemplo de Processamento de Linguagem Natural (NLP) 
# com Reconhecimento de Voz - J.A.R.V.I.S.
> Este é um exemplo simples de um algoritmo de Processamento de Linguagem Natural (NLP) utilizando reconhecimento de voz em Python. O código reconhece comandos de voz específicos e executa ações correspondentes, como abrir programas no sistema operacional Windows.

> Instalação de Bibliotecas
Antes de executar o código, é necessário instalar as seguintes bibliotecas Python:
- speechRecognition: Para reconhecimento de voz.
  - pip install speechRecognition
- pyaudio: Para manipulação de áudio.
  - pip install pyaudio
- pyttsx3: Para síntese de fala.
  - pip install pyttsx3
 
> Utiliza a biblioteca pyttsx3 para inicializar o engine de síntese de fala.
 - Função falar(texto):

> Faz o computador falar o texto fornecido.
 - Função apresentacao():

> Apresenta uma mensagem de inicialização do sistema, tanto no console quanto por meio da síntese de fala.
 - Função ouvir_microfone():

> Habilita o microfone do usuário.
 - Aguarda o usuário falar algo.
 - Reconhece o que foi dito utilizando a API do Google.
 - Executa ação correspondente ao comando reconhecido:
 - Abre o navegador (Google Chrome).
 - Abre a calculadora.
 - Abre o Paint.
 - Abre o bloco de notas.
 - Abre o Excel.
 - Abre o Word.
 - Abre o prompt de comando (CMD).
 - Desliga o sistema.

> Certifique-se de ter todas as bibliotecas instaladas corretamente.
> Execute o script Python em um ambiente compatível com Windows.
> Após a inicialização do sistema, diga um dos comandos reconhecidos pelo programa.

- Obs:. Este código foi projetado para sistemas operacionais Windows e pode não funcionar corretamente em outras plataformas.
- Obs:. Certifique-se de permitir o acesso ao microfone para que o reconhecimento de voz funcione corretamente.

> Este é apenas um exemplo básico de como utilizar reconhecimento de voz para executar ações específicas em Python. Você pode expandir e personalizar este código de acordo com suas necessidades e integrá-lo em projetos mais complexos de automação ou assistentes virtuais.

![texto](jarvis.jpg)
