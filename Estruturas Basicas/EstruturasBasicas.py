# Conversão Tipos Variáveis
idade = "33"
print(idade, type(idade))
idade_inteira = int(idade)
idade_float = float(idade)
altura =  float(input("Digite sua idade, esta será convertida de str para float."))

# Estrutura Repetição while
numero_correto = 8
numero_escolhido = int(input("Digite um número entre zero e dez: "))
while numero_escolhido != numero_correto:
    print("Você errou o número, tente novamente...")
    numero_escolhido = int(input("Digite um número entre zero e dez: "))
print("Parabéns! Acertou o número!")

# Estrura de repetição for
# Na estrura  - range(1, 10, 2) - primeiro parametro é o inicio, o segundo o final e o terceiro de quanto em quanto.
soma = 0
for i in range(1, 5):
    nota = float=(int(input(f"Digite a nota {i}: ")))
    soma = soma + nota
print(soma / 3)

# Listas
primeira_lista = [1.2, 8.5, 6.8, 5.5, 7.9, 5.5]
segunda_lista = [26, "Carlos", 12.5, True] # Multiplos tipos dados
terceira_lista = [33, [12, 25, 87]] # Listas dentro de listas
print(segunda_lista[1]) # Índice Lista/Indexação = imprime o segundo item da lista
print(segunda_lista[-1]) # Acessa o penultimo item da lista
print(primeira_lista[0:3]) # Slice = fatiamento da lista, apresentando somente o solicitado (do indice 0 até menor que 3)
print(primeira_lista[1:]) # apresenta índice dois até o ultimo.
print(primeira_lista[0:5:2]) # Apresenta a lista do item 1 até o quinto item pulando de dois em dois
print(len(primeira_lista)) # Verifica tamanho da lista
primeira_lista.append(5,5) # Adiciona item ao final da lista
primeira_lista.insert(2, 8.8) # Adiciona no índice dois o número 8.8
primeira_lista.extend(segunda_lista) # Agrupa as listas, colocando os elementos da segunda após os da primeira
primeira_lista.pop() # Exclui o ultimo item da lista
primeira_lista.pop(2) # Exclui o elemento de índice dois da lista
primeira_lista.remove(8.5) # Exclui um elemento de uma lista, informando o valor que deseja excluir
primeira_lista.count(5.5) # Conta quantas vezes o item consta na lista
primeira_lista.index(7.9) # Mostra qual o índice do elemento selecionado
primeira_lista.sort() # Ordena a lista de forma crescente
primeira_lista.sort(reverse=True) # Ordena a lista em forma decrescente

# Dicionário - Chave X Valor
dicionario1 = dict() # Cria dicionário vazio
dicionario={"nome":"Carlos", "idade":33} 
print(dicionario[idade]) # Imprime o valor da idade - 33
dicionario["altura"] = 1.80 # Adiciona item ao dicionário
print("peso" in dicionario) # Verifica se o item peso consta no dicionário

# Função
def saudacao(nome, curso):
    print(f"Olá {nome}, bem vindo ao curso de {curso}")
saudacao("Carlos", "Inglês")

def saudacao1(nome, curso="Inglês"): # Coloca-se o valor do curso como default
    print(f"Olá {nome}, bem vindo ao curso de {curso}")
saudacao1("Carlos")


