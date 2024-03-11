# Gerador de Probabilidade de Numeros Sorteados (Mega-Sena ou LotoFacil)

### Simulador de criação de jogos da Mega-Sena ou LotoFacil 
### Gerando a quantidade de jogos "simples" que o usuário solicita, e cria uma probabilidade com números mais sorteados:

- Neste projeto tive de importar a biblioteca ```Random```;
- Na primeira parte crio uma função chamada ```sorteio``` para fazer um jogo simples criando uma lista ```numerosSorteados``` para armazenar esses valores;
- Depois solicito ao usuário que informe a quantidade de sorteios deseja, atribuindo este valor na variável ```quantidadeJogosSorteados```;
- Na terceira parte crio um dicionário ```contadorNumeros``` fazendo um sorteio simpleas a quantidade de vezes informada pelo usuário, e atribuo os valores obtidos no dicionários sendo a chave o número Sorteado e o valor a quantidade de vezes que ele foi sorteado;
- Na quarta parte eu verifico quais os números mais sorteados (Mega-Sena = 6 numeros /  LotoFacil = 15 numeros), usando a função ```sorted``` que verifica no dicionário ```contadorNumeros``` e utiliza uma função lambda para verificar os mais sorteados;
- Na quinta e última parte do código eu imprimo os (seis ou quinze) números mais sorteados, atribuindo às variáveis ```numero``` e ```contagem``` o dicionários obtido na função anterior ```numerosMaisSoretados[i]```: Fazendo a impressão dos números utilizando interpolação de variáveis para melhor exibir o resultado.
