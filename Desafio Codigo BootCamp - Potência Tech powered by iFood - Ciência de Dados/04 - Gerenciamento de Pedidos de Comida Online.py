def main():
 
 n: int = int(input())

 total: float = 0

 for i in range(1, n + 1):
   pedido: str = input().split(" ")
   nome: str = pedido[0]
   valor: float = float(pedido[1])
   total += valor
 desconto: str = input()  
 
 #TODO: Criar as condições para aplicar o cupom de desconto (10% ou 20%).
 
 match desconto:
  case '10%':
   valorDesconto: float = total * 0.1
   total -= valorDesconto
   
  case '20%':
   valorDesconto: float = total * 0.2
   total -= valorDesconto

 print(f'Valor total: {total:.2f}')    
 
 
if __name__ == "__main__":
  main()