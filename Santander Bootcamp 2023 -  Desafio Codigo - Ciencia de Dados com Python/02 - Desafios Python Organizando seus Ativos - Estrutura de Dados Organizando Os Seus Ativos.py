ativos = []

# Entrada da quantidade de ativos
quantidadeAtivos = int(input())

# Entrada dos códigos dos ativos
for i in range(quantidadeAtivos):
    codigoAtivo = input()
    ativos.append(codigoAtivo)

# TODO: Ordenar os ativos em ordem alfabética.
ativos.sort()

# TODO: Imprimir a lista de ativos ordenada, conforme a tabela de exemplos.
for ativo in ativos:
	  print(ativo)