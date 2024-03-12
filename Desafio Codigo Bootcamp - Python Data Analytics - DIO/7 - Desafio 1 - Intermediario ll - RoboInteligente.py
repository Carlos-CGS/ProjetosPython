# TODO: Crie a Função para classificar um número como positivo, negativo ou zero
def classificar_numero(numero):
  if numero > 0:
    return "positivo!"
  else:
    return "negativo!"
    
def main():
    positivos = 0
    negativos = 0
    
    while True:
        numero = int(input())
        
        if numero == 0:
            break  # Encerra o loop se o usuário digitar 0.
        
        # Chama a função classificar_numero para imprimir a classificação do número
        print(classificar_numero(numero))
        
        # TODO: Faça a verificação para saber quantos números positivos e negativos foram inseridos
        if numero > 0:
          positivos += 1
        else:
          negativos += 1 
     
    
    # Imprime a quantidade de números positivos e negativos inseridos
    print(f"{positivos} números positivos, {negativos} números negativos")

if __name__ == "__main__":
    main()