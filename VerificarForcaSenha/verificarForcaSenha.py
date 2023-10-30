# Criação da Função para validar senha
def verificarSenha(password):
    upperChars, lowerChars, specialChars, digits, length = 0,0,0,0,0
    length = len(password)

    #Verifica se a senha possui menos de seis dígitos 
    if (length < 6):
        print("A senha é muito curta. Sua senha deve possuir mais de seis dígitos.")
    else:
        #Caso possua mais de seis dígios, verifica se ela possui letras maiúsculas, 
        # minúsculas, numeros e caracteres especiais, atribuindo valor 1 caso possua.
        for i in range (0, length):
            if (password[i].isupper()):
                upperChars += 1
            elif (password[i].islower()):
                lowerChars += 1
            elif (password[i].isdigit()):
                digits += 1
            else:
                specialChars += 1

    # Verifica se todos os requisitos de validação de senha possuem valor diferente de zero. E após verifica o tamanho da senha.    
    if (upperChars != 0 and lowerChars != 0 and digits != 0 and specialChars != 0):
        if (length >= 10):
            print("A força de sua senha é Forte.")
        else:
            print("A força de sua senha é Média.")

    # Respostas específicas para cada tipo de erro ao criar a senha.
    else:
        if (upperChars == 0):
            print("Senha Fraca! Sua senha deve conter Letra Maiúscula.")
        if (lowerChars == 0):
            print("Senha Fraca! Sua senha deve conter Letra Minúscula.")
        if (digits == 0):
            print("senha Fraca! Sua senha deve conter Número.")
        if (specialChars == 0):
            print("Senha Fraca! Sua senha deve conter Caracter Especial.")

# Solicita a nova senha atribuindo a variavel password e após chama a função verificarSenha    
password = input("Digite sua nova senha!")
verificarSenha(password)
