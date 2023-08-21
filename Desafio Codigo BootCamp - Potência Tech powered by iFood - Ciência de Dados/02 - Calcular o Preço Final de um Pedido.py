valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())

#TODO: Calcular o preço final do pedido (total dos hambúrgueres + total das bebidas).
precoFinal = ((valorHamburguer * quantidadeHamburguer) + (valorBebida * quantidadeBebida))

#TODO: Calcular o troco do pedido, considerando o preço final e o valor pago pelo usuário.
troco = valorPago - precoFinal

#TODO: Imprimir a saída no formato especificado neste desafio.
print(f"O preço final do pedido é R$ {precoFinal:.2f}. Seu troco é R$ {troco:.2f}.")