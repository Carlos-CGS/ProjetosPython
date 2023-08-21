numPedidos: int = int(input())

pedidos: list = []

for i in range(1, numPedidos + 1):
  prato: str = input()
  calorias: int = int(input())
  ehVegano: str = input().strip().lower()
  pedido: dict = {}
  
   #TODO: Tendo em vista a variável booleana "ehVegano", imprima a saída deste desafio.
   
  match ehVegano:
   case "s":
    pedido.update({'Num':i, 'Prato':prato, 'Calorias':calorias, 'E Vegano': '(Vegano)'})
    pedidos.append(pedido)
    
   case "n":
    pedido.update({'Num':i, 'Prato':prato, 'Calorias':calorias, 'E Vegano': '(Nao-vegano)'})
    pedidos.append(pedido)

for pedidos_reg in pedidos:
 print(f'Pedido {pedidos_reg["Num"]}: {pedidos_reg["Prato"]} {pedidos_reg["E Vegano"]} - {pedidos_reg["Calorias"]} calorias')