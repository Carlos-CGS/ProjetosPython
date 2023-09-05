saldo_atual = float(input())
valor_deposito = float(input())
valor_retirada = float(input())

#TODO: Calcular o saldo atualizado de acordo com a descrição deste desafio.
saldo_atualizado = (saldo_atual + valor_deposito) - valor_retirada

#TODO: Imprimir o a saída de conforme a tabela de exemplos (uma casa decimal).
print(f"Saldo atualizado na conta: {saldo_atualizado:.1f}")