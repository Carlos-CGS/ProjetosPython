from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "2024"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n !!! Operação Falou. Você não possui saldo suficiente !!!")
        elif valor > 0:
            self._saldo -= valor
            print("\n$$$ Saldo Realizado com Sucesso. $$$")
            return True
        else:
            print("\n!!! Operação Falou! O valor informado é inválido. !!!")
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n$$$ Depósito Realizado com Sucesso! $$$")
        else:
            print("\n !!! Operação Falhou. O valor informado é inválido. !!!")
            return False
        return True
    
class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=1500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("\n !!! Operação falhou. O valor de saeu excede o limite. !!!")
        elif excedeu_saques:
            print("\n !!! Operação falhou. Numero de saques excedido. !!!")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"""\
            Agência: \t{self.agencia}
            C/C: \t\t{self.numero}
            Titular: \t{self.cliente.nome}
            CPF: \t\t{self.cliente.cpf}
    """
class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )
    
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor
    
    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def menu():
    menu = """ \n
    ======= MENU =======
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar Contas
    [nu]\tNovo Usuário
    [f]\tFinalizar
    ==> """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("!!! Cliente não possui conta. !!!")
        return
    return cliente.contas[0]

def exibir_extrato(clientes):
    cpf = input("Informe o cpf do cliente...")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("!!! Cliente não encontrado. !!!")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("======== EXTRATO =======")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realziadas movimentações até o momento."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"
        
    print(f"CPF: {cliente.cpf}")
    print(f"Cliente: {cliente.nome}")
    print(f"AG: {conta.agencia} - CC:{conta.numero}")
    print("======= ======= =======")
    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")

def criar_cliente(clientes):
    cpf = input("Informe o cpf, inserindo apenas os números...")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("!!! Já existe cliente cadastrado no CPF informado. !!!")
        return
    
    nome = input("Informe o nome completo do novo cliente...")
    data_nascimento = input("Informe a data de nascimento (dd/mm/yyy)...")
    endereco = input("Informe o enderço completo. (Rua, nome, numero, cidade/estado)...")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("=== Cliente criado com Sucesso ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente...")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("!!! Cliente não encontrado. Criação de conta encerrada. !!!")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("=== Conta Criada com Sucesso. ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def sacar_ou_depositar(clientes, valor, tipo_transacao):
    cpf = input("Informe o CPF do cliente...")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("!!! Cliente não encontrado. !!!")
        return
    
    transacao = tipo_transacao(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito..."))
            sacar_ou_depositar(clientes, valor, Deposito)
        elif opcao == "s":
            valor = float(input("Informe o valor do saque..."))
            sacar_ou_depositar(clientes, valor, Saque)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "f":
            break
        else:
            print("!!! Operação Inválida. Tente novamente. !!!")

if __name__ == "__main__":
    main()
