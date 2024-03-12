# Desafios de Código - Python Data Analytics - DIO

Desafio de Código proposto em um BootCamp da plataforma do site DIO, o qual nos faz rever os códigos e complementa-los para que ele alcance os objetivos solicitados.

## Desafio 1 - Básico - Desafios de Código SQUADIO - Iniciante - A Aventura do Explorador

> Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes. Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é desvendando seus caminhos por meio de um código em Python. Prepare-se para a "Aventura do Explorador"!

- Entrada: Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo, representando a quantidade de passos que o explorador deve dar na floresta. .

- Saída: O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta. Utilize um laço de repetição para simular os passos do explorador. A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

> Exemplos: A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.
- Entrada: 2
- Saída: Explorador: 1 passo - Explorador: 2 passos

## Desafio 2 - Básico - Desafios de Código SQUADIO - Iniciante - Lista de itens

> Em um jogo de RPG, os personagens geralmente possuem uma lista de itens que podem ser utilizados durante o jogo. Esses itens podem ser armas, armaduras, poções de cura, entre outros. É importante que o jogador tenha um controle desses itens para poder utilizá-los no momento adequado.
Crie um programa que permita cadastrar uma lista de itens que o personagem possui. A lista deve conter o valor fixo de 3 itens e deve ser exibida na tela.

- Entrada: O programa deve solicitar ao usuário o nome dos 3 itens que o personagem possui. Cada item deve ser cadastrado separadamente.

- Saída: Após receber os itens cadastrados pelo usuário, o programa deve exibir na tela a lista de itens que o personagem possui. A saída deve ter o seguinte formato:

>Lista de itens:
- [item1]
- [item2]
- [item3]

> Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

- Entrada: Espada   Escudo   Poção
- Saída:\
Lista de itens:
  - Espada
  - Escudo
  - Poção         

## Desafio 3 - Básico - Desafios de Código SQUADIO - Iniciante - Armazenamento de Dados é Vida!

> Com as máquinas pesadas agrupadas estrategicamente, graças ao seu algoritmo de cálculo energético, agora a mineração está muito mais eficiente! Com isso, os CodeMiners logo terão que aumentar a capacidade de armazenamento de dados em seus discos de Mithril. Atualmente, cada máquina tem uma capacidade em teraflops e todas terão um upgrade! Escreva um programa que calcule a nova capacidade total de todas as máquinas após um aumento percentual específico.

- Entrada: Dois valores inteiros positivos, representando a capacidade atual total em teraflops e o aumento percentual, separados por espaço.

- Saída: A nova capacidade total em teraflops.

> Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

- Entrada: 100 20
- Saída: 120 

## Desafio 1 - Desafios de Código SQUADIO - Intermediário - O Grande Depósito - Solucionando Problemas Bancários

> Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro. O programa deve solicitar apenas uma vez o valor de depósito.

- Entrada: O programa deve receber o valor de depósito digitado pelo cliente. Os valor pode ser decimal, representando valor em reais.

- Saída: O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Se o valor for "0", deverá imprimir uma mensagem encerrando o programa. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro solicitando um novo valor.

- Entrada: 500.50
- Saída: Deposito realizado com sucesso! / Saldo atual: R$ 500.50

## Desafio 2 - Desafios de Código SQUADIO - Intermediário - Estrutura de Dados: Organizando Os Seus Ativos

> Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

- Entrada: A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, os tipos (strings) dos respectivos ativos.

- Saída: Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.

- Entrada: 3  /  Financiamento de Imovel  /  Deposito  /  Reservas Bancarias
- Saída: 	Deposito  /  Financiamento de Imovel  /  Reservas Bancarias

## Desafio 3 - Desafios de Código SQUADIO - Intermediário - Validando a Força de Senhas no IAM

> Você está trabalhando para uma empresa que utiliza extensivamente os serviços da AWS, e após algumas análises a equipe de segurança identificou que algumas senhas dos usuários no IAM são fracas e podem representar um risco à segurança dos dados da empresa. Para resolver esse problema, foi solicitado que você desenvolva um programa capaz de analisar as senhas dos usuários e fornecer uma validação de força com base em critérios predefinidos.

 - Requisitos de segurança para a senha:\
    A senha deve ter no mínimo 8 caracteres.\
    A senha deve conter pelo menos uma letra maiúscula (A-Z).\
    A senha deve conter pelo menos uma letra minúscula (a-z).\
    A senha deve conter pelo menos um número (0-9).\
    A senha deve conter pelo menos um caractere especial, como !, @, #, $, %, etc.\
    Saiba mais sobre o Regex em: Java Regular Expressions

- Entrada: A entrada será uma única string representando a senha que precisa ser validada.

- Saída: Seu programa deve retornar uma mensagem indicando se a senha fornecida pelo usuário atende aos requisitos de segurança ou não, juntamente com um feedback explicativo sobre os critérios considerados.

- Entrada: 0101
- Saída: Sua senha e muito curta. Recomenda-se no minimo 8 caracteres.

## Desafio 1 - Desafios de Código SQUADIO - Intermediário ll - O Robô inteligente

> Você foi contratado pela empresa DIO Robots para programar um robô capaz de classificar números em uma das seguintes categorias: negativo, positivo ou zero. Para isso, você deve criar uma função de classificação que receba um número como parâmetro e retorne a mensagem "negativo!" ou " positivo!", de acordo com sua categoria.

> O programa deve ser executado continuamente, permitindo que o usuário insira vários números. Quando ele quiser encerrar a execução, deverá digitar um número igual a zero. A cada novo número inserido, o robô deve classificá-lo e exibir a mensagem correspondente. Ao final da execução, o programa deverá exibir a quantidade de números positivos, negativos e zeros que foram inseridos.

- Entrada: A entrada deve receber valores inteiros.

- numero: valor inteiro que pode ser positivo, negativo ou zero. Lembrando que a entrada zero deve encerrar o programa.

- Saída: O código deverá retornar uma mensagem (string) informando se o número é positivo ou não. Ao receber o valor 0, ele deverá encerrar o e informar quantos números foram positivos e negativos.

- Entrada:	1  /  -1  /  2  /  0
- Saída: positivo!  /  negativo!  /  positivo!  /  2 números positivos, 1 números negativos

## Desafio 2 - Desafios de Código SQUADIO - Intermediário ll - A Jornada da Classificação Frutífera

> Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

- Maçã:
  Peso mínimo: 130 gramas
  Textura: Ápera (rough)
  Cor: Vermelha (red)

- Laranja:
  Peso mínimo: 120 gramas
  Textura: Suave (smooth)
  Cor: Laranja (orange)

- Morango:
  Peso mínimo: 150 gramas
  Textura: Suave (smooth)
  Cor: Vermelha (red)

- Banana:
  Peso mínimo: 150 gramas
  Textura: Áspera (rough)
  Cor: Amarela (yellow)

- Entrada: Seu código deve receber as seguintes entradas do usuário:

- Peso da fruta (em gramas): um número real que representa o peso da fruta.
- Textura da fruta (suave ou áspera): uma string indicando se a fruta é suave ("smooth") ou áspera ("rough").
- Cor da fruta (vermelha, laranja ou amarela): uma string indicando a cor da fruta.

- Saída: O código deve produzir uma saída indicando a classificação da fruta com base nas características fornecidas.

- Entrada:	150  /  smooth  / red	
- Saída: A fruta é um morango!

## Desafio 3 - Desafios de Código SQUADIO - Intermediário ll - A Questão Intrincada da Magia Preditiva

> No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.

- Aqui estão os critérios mágicos para cada elemento:

> Elemento Fogo:
  Intensidade do feitiço maior ou igual a 5.
  Fase lunar durante o feitiço é crescente.
  Idade do feiticeiro é superior a 100 anos.

> Elemento Água:
  Intensidade do feitiço maior ou igual a 7.
  Presença de componente raro.
  Fase lunar durante o feitiço é cheia.
  Idade do feiticeiro é igual ou inferior a 100 anos.
  Afinidade com animais mágicos.

> Elemento Terra:
  Intensidade do feitiço maior ou igual a 7.
  Presença de componente raro.
  Fase lunar durante o feitiço é cheia.
  Idade do feiticeiro é igual ou inferior a 100 anos.
  Afinidade com animais mágicos.

> Elemento Ar:
  Caso não se encaixe nos critérios anteriores.

- Entrada: Seu código deve receber as seguintes entradas do usuário:

- Intensidade do feitiço (de 1 a 10): um número inteiro representando a força do feitiço.
- Componente raro (sim ou não): uma string indicando se o feitiço contém um componente raro.
- Fase lunar (cheia, crescente ou minguante): uma string indicando a fase lunar durante o lançamento do feitiço.
- Idade do feiticeiro (em anos): um número inteiro representando a idade do feiticeiro.
- Afinidade com animais mágicos (sim ou não): uma string indicando se o feiticeiro tem afinidade com animais mágicos.

- Saída: O código deve produzir uma saída indicando a afinidade elemental prevista do feiticeiro com base nos atributos fornecidos.

- Entrada:	6  /  sim  /  crescente110  /  sim	
- Saída: A afinidade elemental do feiticeiro é com o elemento Fogo!