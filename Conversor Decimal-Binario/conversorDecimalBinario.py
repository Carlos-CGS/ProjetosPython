# Conversor de Decimal para Binário Utilizando o conceito de Pilha criado dentro de uma classe contruída em Python
import os

class Pilha():
    def __init__(self):
        self.data = []

    #Adiciona os itens ao topo da lista
    def push(self, x):
        self.data.append(x)

    #Remove os item do topo da lista
    def pop(self):
        if len(self.data) > 0:
            return self.data.pop(-1)

    #Retorna o item do topo da lista    
    def top(self):
        if len(self.data) > 0:
            return self.data[-1]

    #Verifica se a lista esta vazia    
    def empty(self):
        return not len(self.data) > 0

p = Pilha()
os.system("cls") or None
numeroEscolhido = int(input("Digite um numero para ser convertido... "))
num = numeroEscolhido
resultado = []

while num > 0:
    resto = num % 2
    num = num // 2
    p.push(resto)

while not p.empty():
    resultado.append(p.pop())

print(f"O número {numeroEscolhido} em binário é {resultado}")