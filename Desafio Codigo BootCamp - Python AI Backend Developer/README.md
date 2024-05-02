# Desafios de Código - Python AI Backend Developer

- Desafio de Código proposto em um BootCamp da plataforma do site DIO, o qual nos faz rever os códigos e complementa-los para que ele alcance os objetivos solicitados.

## Desafio 1 - Explorando POO com Python - Criando uma Classe de Usuário
> Vamos criar uma classe chamada UsuarioTelefone para representar um usuário de telefone. Você pode definir um método especial e depois aplicar conceitos de encapsulamento nos atributos dentro da classe. Lembre-se que, cada usuário terá um nome, um número de telefone e um plano associado, neste desafio, simulamos três planos, sendo: Plano Essencial Fibra, Plano Prata Fibra e Plano Premium Fibra.

- Entrada: Nome do usuário, número de telefone e plano.

- Saída: Mensagem indicando que o usuário foi criado com sucesso.

- Entrada:	Ana     /     (11) 91111-1111     /     Plano Essencial Fibra

- Saída: Usuário Ana criado com sucesso.

## Desafio 2 - Explorando POO com Python - Adicionando Funcionalidades ao Plano
> Agora, vamos Adicionar uma funcionalidade à classe UsuarioTelefone para que possa ser verificado o saldo disponível em seu plano. Para essa solução, você pode criar uma classe PlanoTelefone, o seu método de inicialização e encapsular os atributos, 'nome' e 'saldo' dentro da classe. Adicione também um método 'verificar_saldo' para verificar o saldo do plano e uma  'mensagem_personalizada' para gerar uma mensagem personalizada.

> Condições da verificação do saldo:
- Caso o saldo seja menor do que 10, retorne: "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
- Caso o saldo seja maior ou igual a 50, retorne: "Parabéns! Continue aproveitando seu plano sem preocupações."
- Caso contrário, retorne: "Seu saldo está razoável. Aproveite o uso moderado do seu plano."

- Entrada: Como entrada, será solicitado o nome, plano (Essencial, Prata, Premium) e saldo atual do cliente.

- Saída: Mensagem personalizada de acordo o saldo do cliente.

- Entrada:	João     /     Essencial      /     9

- Saída: Seu saldo está baixo. Recarregue e use os serviços do seu plano.

## Desafio 3 - Explorando POO com Python - Realizando Chamadas
> Vamos agora, adicionar uma funcionalidade à classe UsuarioTelefone, que realizar chamadas para outros usuários. Cada chamada terá uma duração em minutos e o custo será deduzido do saldo do usuário, suponha o custo de $0.10 por minuto. Você pode criar um método fazer_chamada que vai permitir que o usuário faça a chamada, ele vai receber o destinatario e duracao como parâmetros. Calcule o custo da chamada usando o método 'custo_chamada' do objeto 'plano', além de adicionar o método deduzir_saldo para deduzir o valor do saldo do plano e depois retorne uma mensagem adequada como mostra no exemplo a baixo.

- Entrada: Número do usuário, número do telefone, saldo inicial, número do destinatário e a duração da chamada em minutos.

- Saída: Mensagem indicando o sucesso da chamada ou saldo insuficiente para fazer a chamada.

- Entrada:	Rodrigo   /   (00) 90000-0000   /   10.00   /   (33) 93333-3333   /   60

- Saída: Chamada para (33) 93333-3333 realizada com sucesso. Saldo: $4.00