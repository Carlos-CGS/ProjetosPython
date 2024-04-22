# Projeto Jogo da Forca com Pyhthon

### Biblioteca Utilizada - random
### Projeto simples de um jogo da forca que faz um sorteia entre as palavras de uma lista.

- Antes de mais nada eu importo a biblioteca ```random```;
- Depois crio uma função ```escolher_palavra``` crio uma lista contendo palavras p´re escolhidas por mim para serem possiveis palavras do game, a seguir utilizo o método ```random.choice``` para sortear uma palavra da lista criada;
- Na terceira parte do código eu crio a função jogar_forca;
 - defino a variável palavra, atribuindo a ela o chamdo do método ```escolher_palavra```, assim como criar listas zerada para ```letras_erradas``` e adiconar a palavra selecionada na lista ```letras_corretas```, além da criação das variaveis ```tentativas``` que defini a quantidade de vezes que o usuário pode errar e ```ponto``` que diminiu dez pontos a cada erro cometido pelo usuário;
 - Crio dois prints para exibir uma mensagem de inicio de jogo;
 - Depois utilizo um ```while``` para vrificar a quantidade de letras e adicionar a mesma quantidade de ```_``` na variável ```palavra_secreta```;
 - Imprimo a ```palavra_secreta``` parcial ao usuário, onde só é informado as letras que ele acertou;
 - Após utilizo um ```if``` para verificar se todas as letras informadas pelo usuário são iguais a variável ```palavra```;
 - Solicito ao usuário que insira uma letra e a atribuo a variável ```tentativa```;
 - Verifico se a letra atribuída a ```tentativa``` esta contido em ```palavra```. Se sim, adiciona a letra na variável ```letras_corretas``` através do método ```.append```;
 - Informa ao usuário Letra Correta.
 - Caso não esteja contido, adiciona a variável ```letras_erradas``` a ```tentativa``` informada pelo usuário, decrementa ```tentativas``` em -1, e decrementa ```ponto``` em -10;
 - Informa a quantidade de tentativas restantes;
 - E para finalizar utilizo um ```if``` para evricar se ```tentativas``` é igual a 0, e se for, encerra o programa, infomando que o usuário perdeu o jogo!
 -Chamo o ```main``` que chama a função ```jogar_forca```.


