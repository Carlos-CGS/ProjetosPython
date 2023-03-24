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
