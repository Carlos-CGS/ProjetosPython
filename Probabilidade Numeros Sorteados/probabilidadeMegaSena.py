import random

#Sorteia seis números em um jogo simples
def sorteio():
  numerosSorteados = []
  for i in range(6):
    numero = random.randint(1, 60)
    numerosSorteados.append(numero)
  return numerosSorteados

#Solicita ao usuário a quantidade de sorteios
quantidadeJogosSorteados = int(input("Informe quantas jogos devem ser feitos para a estatística..."))

# Dicionário para Armazenar os numeros mais sorteados
contadorNumeros = {}
for i in range (quantidadeJogosSorteados):
  jogoFeito = sorteio()
  for numero in jogoFeito:
    contadorNumeros [numero] = contadorNumeros.get(numero, 0) + 1

#Verifica os seis numeros mais sorteados
numerosMaisSorteados = sorted(contadorNumeros.items(), key=lambda x: x[1], reverse=True )

#Imprimi os seis numeros mais sorteados
print("Os seis números mais sorteados foram:")
for i in range (6):
  numero, contagem = numerosMaisSorteados[i]
  print(f"{i+1}° Número: {numero} - Soteado {contagem} vezes")
 