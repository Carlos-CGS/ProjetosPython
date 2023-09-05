# Desafios de Código Santander Bootcamp 2023 - Ciência de Dados com Python

- Desafio de Código proposto em um BootCamp da plataforma do site DIO, o qual nos faz rever os códigos e complementa-los para que ele alcance os objetivos solicitados.

## Desafio 1 -  Equilibrando Saldo - Variáveis em Ação: Equilibrando o Saldo

> Descrição:\
Para esse desafio, considere que você foi contratado por uma empresa bancária para auxiliar nas implementações e melhorias do sistema empresarial. Em uma análise inicial, foi identificado pela equipe financeira a necessidade de desenvolver uma solução que permita ao cliente equilibrar seu saldo bancário. Dessa forma, o programa deve solicitar uma entrada que representa o saldo atual do funcionário, e após, seja informado o valor de duas transações, sendo elas: um depósito e um saque. O programa deve atualizar o saldo com base nas transações e exibir o saldo final.

Informação: As transações de depósito e retirada devem ser tratadas como valores positivos e negativos, respectivamente, para garantir que o cálculo do saldo final seja realizado corretamente.

- Entrada:\
saldoAtual: um número decimal representando o saldo atual da conta bancária.\
valorDeposito: um número decimal representando o valor a ser depositado na conta.\
valorRetirada: um número decimal representando o valor a ser retirado da conta.\
  1000\
  500\
  200

  Regra de Formatação: Considere apenas uma casa decimal para esse desafio.

- Saída:  \
Um número decimal que representa o saldo atualizado na conta bancária após o processamento das transações.\
  Saldo atualizado na conta: 1300.0


## Desafio 2 - Organizando seus Ativos - Estrutura de Dados: Organizando Os Seus Ativos

> Após uma análise cuidadosa realizada pela equipe de desenvolvimento de uma empresa bancaria, foi identificado a necessidade de uma nova funcionalidade para otimizar os processos e melhorias da experiência dos usuários. Agora, sua tarefa é implementar uma solução que organize em ordem alfabética uma lista de ativos que será informada pelos usuários. Os ativos são representados por strings que representam seus tipos, como por exemplo: Reservas de liquidez, Ativos intangiveis e dentre outros.

- Entrada: A primeira entrada consiste em um número inteiro que representa a  quantidade de ativos que o usuário possui. Em seguida, o usuário deverá  informar, em linhas separadas, os tipos (strings) dos respectivos ativos:\
   3\
   Financiamento de Imovel\
   Deposito\
   Reservas Bancarias

- Saida: Seu programa deve exibir a lista de Ativos organizada em ordem alfabética. Cada ativo deve ser apresentado em uma linha separada.\
Deposito\
Financiamento de Imovel\
Reservas Bancarias

## Desafio 3 - Condicionalmente Rico - Condicionalmente Rico: Tomadas de Decisão no Código

> Uma nova feature para um sistema bancário foi analisada pela equipe de desenvolvimento e será uma das tarefas a serem trabalhadas durante a sprint, como desenvolvedor da empresa você recebeu os requisitos para a nova implementação que consiste em uma solução algorítmica que permita aos clientes realizarem saques em caixas eletrônicos. No entanto, existem algumas regras a serem seguidas para garantir que um saque possa ser realizado com sucesso.

Regras do saque:

Cada cliente digitará o valor do seu saldoTotal de sua conta bancária e o valorSaque.\
Um saque só pode ser realizado se o saldoDisponível na conta for igual ou superior ao valor solicitado.\
Se o saldo for suficiente, o valor solicitado deve ser subtraído do saldo disponível, indicando que o saque foi realizado.\
Se o saldo for insuficiente, o saque não deve ser realizado e uma mensagem adequada deve ser exibida.

- Entrada\
A entrada consiste em dois valores inteiros que representam o total do saldo da conta e o valor do saque.\
1000\
200

- Saída
Se o saque for realizado com sucesso, exibir a mensagem "Saque realizado com sucesso! Novo saldo: {saldo}", onde {saldo} é o novo saldo disponível na conta.\
  Se o saque não for possível devido a saldo insuficiente, exibir a mensagem "Saldo insuficiente. Saque nao realizado!"
  Saque realizado com sucesso! Novo saldo: 800

## Desafio 4 - Juros Compostos - Juros Compostos

> Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu objetivo é criar uma função que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de tempo em anos. A função deve calcular e retornar o valor final do investimento após o período determinado, levando em consideração os juros compostos.

- Entrada: \
A função deve receber os seguintes parâmetros:

  valor_inicial: um número inteiro ou decimal representando o valor inicial do investimento.

  taxa_juros: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.

  periodo: um número inteiro representando a quantidade de anos do investimento.\
  5000   ----   0.08     ----  5
- Saída:\
 A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final deve ser arredondado para duas casas decimais.
 Valor final do investimento: R$ 7346.64

## Desafio 5 - O Grande Depósito - O Grande Depósito - Solucionando Problemas Bancários

> Você foi contratado por um banco para desenvolver um programa que auxilie seus clientes a realizar depósitos em suas contas. O programa deve solicitar ao cliente o valor do depósito e verificar se o valor é válido. Se o valor for maior do que zero, o programa deve adicionar o valor ao saldo da conta. Caso contrário, o programa deve exibir uma mensagem de erro e solicitar um novo valor. O programa deve continuar solicitando valores de depósito até que seja digitado um valor válido.

- Entrada: 
O programa deve utilizar o Scanner para receber os valores de depósito digitados pelo cliente. Os valores podem ser decimais, representando valores em reais.\
500.50

- Saída: 
O programa deve exibir uma mensagem de sucesso quando um valor de depósito válido for informado e o saldo da conta for atualizado. Caso um valor inválido seja digitado, o programa deve exibir uma mensagem de erro e solicitar um novo valor.\
Deposito realizado com sucesso!
Saldo atual: R$ 500.50