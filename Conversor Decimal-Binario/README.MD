# Conversor de Decimal para Binário Utilizando o conceito de Pilha em Python
## Pilha em python é alocar um valor de forma a empilhar um em cima do outro na memória.
### Para explicar melhor, posso fazer uma analogia como se fosse uma pilha de pratos, onde só conseguimos retirar o ultimo prato adicionado em cima da pilha, pois se tentarmos retirar o primeiro adiconado toda a pilha desmorona.

>  conversor de números decimais para binários usando o conceito de pilha. A pilha é uma estrutura de dados que segue a regra "último a entrar, primeiro a sair" (LIFO - Last In, First Out).

-  O código começa com a definição de uma classe chamada Pilha, que será responsável por representar a estrutura de pilha. 

> Em seguida, são definidos métodos para adicionar elementos (push), remover elementos (pop), verificar o elemento no topo (top) e verificar se a pilha está vazia (empty).

> Após a definição da classe Pilha, o código principal cria uma instância dessa classe (p = Pilha()) e solicita que o usuário insira um número decimal a ser convertido.

> Em seguida, o código calcula o equivalente binário do número decimal inserido pelo usuário. Ele usa o algoritmo de divisão sucessiva por 2 para calcular os dígitos binários.

> O resultado binário é armazenado na pilha p. Posteriormente, os elementos são removidos da pilha e armazenados em uma lista chamada resultado.

> Finalmente, o código exibe o número decimal original e seu equivalente binário.