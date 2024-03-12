# Desafio: A Aventura do Explorador

# Entrada
quantidade_passos = int(input())

# TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
# Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
# Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

if quantidade_passos > 0:
  palavraPasso = "passo"
  
  for i in range(quantidade_passos):
    if i > 0:
      palavraPasso = "passos"
    print("Explorador: ", i+1, palavraPasso)
    
else: print("Nenhum passo dado na floresta.")