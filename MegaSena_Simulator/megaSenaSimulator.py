import random

numeroSorteado = [
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60),
    random.randrange(1,60)
]

print("Primeira sequancia de números a serem jogados: ", 
      numeroSorteado[0], 
      numeroSorteado[1], 
      numeroSorteado[2], 
      numeroSorteado[3], 
      numeroSorteado[4], 
      numeroSorteado[5])


# Abaixo, será apresentado o mesmo código aciam, porém feito de forma correta.

# A função sorted faz ordena os números, e o demais gera uma lista de seis números aleatórios
numeroSorteado1 = sorted(random.sample(range (1,61), 6))
# Concatenei uma string com todos os números sorteados utilizando o *
print("Segunda sequencia de números a serem jogados: ", *numeroSorteado1)
