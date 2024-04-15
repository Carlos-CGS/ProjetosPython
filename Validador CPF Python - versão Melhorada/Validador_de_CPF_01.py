import re

def validador():
    cpf = input("Digite um CPF para ser validado ao lado. >>>")

    # Retira apenas os dígitos do CPF, ignorando os caracteres especiais
    numeros = [int(digito) for digito in cpf if digito.isdigit()]
    
    formatacao = False
    quant_digitos = False
    validacao1 = False
    validacao2 = False

    # Verifica a estrutura do CPF (111.222.333-44) ou (11122233344)
    if re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf) or re.match(r'\d{11}', cpf):
        formatacao = True

    if len(numeros) == 11:
        quant_digitos = True
    
        soma_produtos = sum(a * b for a, b in zip(numeros[0:9], range(10, 1, -1)))
        digito_esperado = (soma_produtos * 10 % 11) % 10
        if numeros[9] == digito_esperado:
            validacao1 = True

        soma_produtos1 = sum(a * b for a, b in zip(numeros[0:10], range(11, 1, -1)))
        digito_esperado1 = (soma_produtos1 * 10 % 11) % 10
        if numeros[10] == digito_esperado1:
            validacao2 = True

        if quant_digitos and formatacao and validacao1 and validacao2:
            print(f"O CPF {cpf} é válido.")
        else:
            print(f"O CPF {cpf} não é válido... Tente outro CPF...")

        # Verificação dos estados de origem do CPF
        estado_origem = numeros[8]
        estados = {
            1: "Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins",
            2: "Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima",
            3: "Ceará, Maranhão ou Piauí",
            4: "Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas",
            5: "Bahia ou Sergipe",
            6: "Minas Gerais",
            7: "Rio de Janeiro ou Espírito Santo",
            8: "São Paulo",
            9: "Paraná ou Santa Catarina"
        }
        if estado_origem in estados:
            print(f"Seu CPF é originário do estado de {estados[estado_origem]}.")
        else:
            print("Seu CPF é de origem do estado do Rio Grande do Sul")

    else:
        print(f"O CPF {cpf} não é válido... Tente outro CPF...")

validador()
