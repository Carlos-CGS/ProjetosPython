from configparser import SafeConfigParser
from pydoc import safeimport


MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Digite sua Idade!'))

if idade >= MAIOR_IDADE:
    print('Voce pode inicar o processo para tirar CNH!')
else:
    print('Voce ainda não pode tirar sua CNH!')

if idade >= MAIOR_IDADE:
    print('Maior Idade, pode tirar sua CNH ! Processo prático e teórico iniciado')
elif idade == IDADE_ESPECIAL:
    print('Voce pode iniciar o processo teórico')
else:
    print('Voce ainda não pode iniciar o processo para obtenção da CNH!')


# Exemplo de IF Ternário abaixo
saldo = 1000
saque = 500
status = 'Sucesso!' if saldo >= saldo else "Falha"
print(f"{status} ao realizar o saque")


#Abaixo exemplo de estrutura de repetição FOR (ITERÁVEL), onde upper faz as letras ficarem maiúsculas
#Abaixo uma estrutura de repetição que apresenta as vogais da palavar digitada.
texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='') # <<< end'' << serve para colocar o resultado um do lado do outro na saída
print()

#Abaixo uma estrura de repetição (FOR/RANGE)
for numero in range(0,51,5):
    if numero == 15:
        continue # Exemplo do uso do continue (quando o numero for igual ao mencionado nn apresenta o resultado)
    print(numero)

#Abaixo estrutura de repetição (WHILE)
numero = -1
while numero != 0:
    numero = int(input('[1] Sacar \n[2] Depositar \n[0] Sair'))
    if numero == 1:
        print("Sacando")
    elif numero == 2:
        print('Depositando')

    elif numero == 7:
        break  # << Exemplo do uso do break

    else:
        print('Obrigado por utilizar nossos caixas!')


#Interpolação de Variáveis
nome = "Carlos"
idade = 28 
dinheiro = 288495.8
   
    # Primeira forma ( % )
print("Olá, meu nome é %s e tenho %d anos de idade e tenho %f reais." %(nome, idade, dinheiro))

    #Segunda forma ( .format ) - 4 formas
print("Olá, meu nome é {}, tenho {} anos de idade e tenho {} reais" .format(nome, idade, dinheiro))

print("Olá, meu nome é {1}, tenho {2} anos de idade e tenho {0} reais" .format(dinheiro, nome, idade))

print("Olá, meu nome é {name}, tenho {idade} anos de idade e tenho {dinheiro} reais" .format(name=nome, idade=idade, dinheiro=dinheiro))

dados = {"nome": "Carlos", "idade": 28, "dinheiro": 2345.856}
print("Olá, meu nome é {nome}, tenho {idade} anos e tenho {dinheiro} reais" .format(**dados))
    
    #Terceira Forma (f string )
print(f"Olá, meu nome é {nome}, tenho {idade} anos e tenho {dinheiro} reais")

    #Definir tamanho de casas decimais
print(f"Olá, meu nome é {nome}, tenho {idade} anos e tenho {dinheiro:.2f} reais") # para definir apenas duas casas decimais após virgula
print(f"Olá, meu nome é {nome}, tenho {idade} anos e tenho {dinheiro: 10.2f} reais") # para definir 10 espaços em branco e duas casas decimais após virgula

    #Exemplo de fatiamento de string invertendo as letras
teste = "Carlos Garcia"
print(teste[:: -1])

    #String de múltiplas linhas
mensagem = ("""
    --- #### Menu ####---
         1 - Sacar 
         2 - depositar
         3 - sair 
""")
print (mensagem)


# Compreensaõ de dados de duas formas:
numeros = [1, 2, 3, 4, 5, 6]

#exemplo 1
pares = [] # cria-se uma nova lista
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

print(pares)

#exemplo 2
pares1 = [numero for numero in numeros if numero % 2 == 0]
print(pares1)

#Modificando Valores de uma Lista
numeros=[1, 2, 3, 4, 5, 6]

#Exemplo_1
quadrado=[]
for numero in numeros:
    quadrado.append(numero ** 2)
print(quadrado)

#Exemplo_2
quadrado1=[numero ** 2 for numero in numeros]
print(quadrado1)

