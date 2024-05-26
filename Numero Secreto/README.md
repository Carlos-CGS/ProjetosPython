# Jogo de Adivinhação com Reconhecimento de Voz

Este é um jogo simples de adivinhação de número secreto de 1 a 100, que utiliza reconhecimento de voz para interação com o usuário.

## Bibliotecas Utilizadas

- `speech_recognition`: Para capturar e interpretar a fala do usuário.
- `pyttsx3`: Para sintetizar a fala e fornecer feedback de voz.

## Funções

### `ouvir_microfone()`

Esta função captura a entrada de voz do usuário, ajusta o ruído ambiente e tenta reconhecer a fala usando o Google Speech Recognition.

- Parâmetros: Nenhum.
- Retorno: A frase reconhecida como uma string ou `None` se não foi possível entender a fala.

### `falar(texto)`

Esta função sintetiza a fala do programa usando o pyttsx3.

- Parâmetros: `texto` - A string a ser falada.
- Retorno: Nenhum.

### `apresentacao()`

Esta função imprime uma mensagem de introdução e instruções ao jogador.

- Parâmetros: Nenhum.
- Retorno: Nenhum.

### `jogo_adivinhacao()`

Esta função contém a lógica principal do jogo. Um número secreto é gerado aleatoriamente e o jogador tem que adivinhá-lo.

- Parâmetros: Nenhum.
- Retorno: Nenhum.

## Lógica do Jogo

1. O número secreto é gerado aleatoriamente entre 1 e 100.
2. O jogador é solicitado a adivinhar o número secreto usando sua voz.
3. O programa fornece feedback de voz se a tentativa do jogador é maior, menor ou igual ao número secreto.
4. O jogo continua até que o jogador adivinhe corretamente o número secreto.
5. O programa informa ao jogador quantas tentativas foram necessárias para adivinhar o número secreto.

## Execução do Código

O código é executado no final, chamando primeiro a função `apresentacao()` para apresentar as instruções ao jogador e em seguida a função `jogo_adivinhacao()` para iniciar o jogo.

```python
if __name__ == "__main__":
    apresentacao()
    jogo_adivinhacao()
