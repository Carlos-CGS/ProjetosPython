menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[f] Fim/Sair

=> """

saldo = 0
limite = 500
extrato = ""
numeroSaques = 0

LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"       Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor de saque: "))

        excedeuSaldo = valor > saldo
        excedeuLimite = valor > limite
        excedeuSaques = numeroSaques >= LIMITE_SAQUES

        if excedeuSaldo:
            print("Operação falou! Você não tem saldo suficiente.")

        elif excedeuLimite:
            print("Operação falou! O valor do saque excedeu o limite.")

        elif excedeuSaques:
            print("Operação falou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"       Saque: R$ {valor:.2f}\n"
            numeroSaques += 1

        else:
            print("Operação falou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n=============EXTRATO===============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n       Saldo: R$ {saldo:.2f}")
        print("*************************************")

    elif opcao == "f":
        break

    else:
        print("Operação inválida, por favor selecione corretamnete a opção desejada.")