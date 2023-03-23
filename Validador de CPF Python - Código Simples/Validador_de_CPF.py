# Criado abaixo uma função para validar um CPF digitado.
NOVO_CPF = list(input("Digite um CPF para ser validado >>>"))
NOVO_CPF_STRING = " ".join(NOVO_CPF)

def validacao_cpf():
    if len(NOVO_CPF) == 11:
        primeiro1 = int(NOVO_CPF[0]) * 10
        primeiro2 = int(NOVO_CPF[1]) * 9
        primeiro3 = int(NOVO_CPF[2]) * 8
        primeiro4 = int(NOVO_CPF[3]) * 7
        primeiro5 = int(NOVO_CPF[4]) * 6
        primeiro6 = int(NOVO_CPF[5]) * 5
        primeiro7 = int(NOVO_CPF[6]) * 4
        primeiro8 = int(NOVO_CPF[7]) * 3
        primeiro9 = int(NOVO_CPF[8]) * 2

        seg_primeiro1 = int(NOVO_CPF[0]) * 11
        seg_primeiro2 = int(NOVO_CPF[1]) * 10
        seg_primeiro3 = int(NOVO_CPF[2]) * 9
        seg_primeiro4 = int(NOVO_CPF[3]) * 8
        seg_primeiro5 = int(NOVO_CPF[4]) * 7
        seg_primeiro6 = int(NOVO_CPF[5]) * 6
        seg_primeiro7 = int(NOVO_CPF[6]) * 5
        seg_primeiro8 = int(NOVO_CPF[7]) * 4
        seg_primeiro9 = int(NOVO_CPF[8]) * 3
        seg_primeiro10 = int(NOVO_CPF[9]) * 2

        soma_validacao = (primeiro1 + primeiro2 + primeiro3 + primeiro4 + primeiro5 + primeiro6 + primeiro7 + primeiro8 + primeiro9)
        divisao_soma = (soma_validacao // 11)
        resto = (soma_validacao - (11 * divisao_soma))

        soma_validacao_2 = (seg_primeiro1 + seg_primeiro2 + seg_primeiro3 + seg_primeiro4 + seg_primeiro5 + seg_primeiro6 + seg_primeiro7 + seg_primeiro8 + seg_primeiro9 + seg_primeiro10)
        divisao_soma_2 = (soma_validacao_2 // 11)
        resto_2 = (soma_validacao_2 - (11 * divisao_soma_2))
        
        antepenultimo_digito_cpf = int(NOVO_CPF[8])
        penultimo_digito_cpf = int(NOVO_CPF[9])
        ultimo_digito_cpf = int(NOVO_CPF[10])

        val_1 = False
        val_2 = False
        val_3 = False
        val_4 = False

        if(resto <=1) and (penultimo_digito_cpf == 0):
            val_1 = True
        if( resto >=2 and resto < 10) and (11 - resto == penultimo_digito_cpf):
            val_2 = True
        if( resto_2 <=1 ) and (ultimo_digito_cpf == 0):
            val_3 = True
        if ( resto_2 >=2 and resto_2 < 10 ) and (11 - resto_2 == ultimo_digito_cpf):
            val_4 = True
        else: ()

        if (val_1 == True or val_2 == True) and (val_3 == True or val_4 == True):
            print(f"O CPF número: {NOVO_CPF_STRING} é válido !")
        else:
            print(f"O CPF número: {NOVO_CPF_STRING} é inválido, tente novamente.")

        #Abaixo Validação dos estado de origem do CPF
        if antepenultimo_digito_cpf == 1:
            print("Seu CPF é originário do estado do Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
        elif antepenultimo_digito_cpf == 2:
            print("Seu CPF é originário do estado do Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima")
        elif antepenultimo_digito_cpf == 3:
            print("Seu CPF é originário do estado do Ceará, Maranhão ou Piauí")
        elif antepenultimo_digito_cpf == 4:
            print("Seu CPF é originário do estado de Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas")
        elif antepenultimo_digito_cpf == 5:
            print("Seu CPF é originário do estado da Bahia; e Sergipe")
        elif antepenultimo_digito_cpf == 6:
            print("Seu CPF é originário de Minas Gerais")
        elif antepenultimo_digito_cpf == 7:
            print("Seu CPF é originário do estado do Rio de Janeiro ou Espírito Santo")
        elif antepenultimo_digito_cpf == 8:
            print("Seu CPF é originário do estado de São Paulo")
        elif antepenultimo_digito_cpf == 9:
            print("Seu CPF é originário do estado do Paraná ou Santa Catarina")
        else:
            print("Seu CPF é de origem do estado do Rio Grande do Sul")

    else: 
        print(f"O CPF número: {NOVO_CPF_STRING} é inválido, tente novamente.")

validacao_cpf()