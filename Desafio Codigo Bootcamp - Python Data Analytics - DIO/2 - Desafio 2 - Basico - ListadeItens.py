# Lista para armazenar os itens
itens = []

# TODO: Solicite os itens ao usuário 
# Primeira forma de se fazer a solução deste Desafio:
item1 = input()
item2 = input()
item3 = input()
itens.append(item1)
itens.append(item2)
itens.append(item3)
# Segunda forma de se fazer a solução Deste Desafio:
for i in range(3):
    item = input("Digite o item: ")
    itens.append(item)


# Exibe a lista de itens
print("Lista de itens:")
for item in itens:
    print(f"- {item}")