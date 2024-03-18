def desencriptar():
    senha = input("Digite sua senha ENCRIPTADA PARA DESENCRIPTAR...")
    tamanhoSenha = len(senha)
    listaSenha = []
    for letra in senha:
        listaSenha.append(letra)
    
    # Desmbaralha alguns caracteres
    listaAntiga  = list(listaSenha)
    listaSenha[-1] = listaAntiga[0]
    listaSenha[0] = listaAntiga[-1]
    listaSenha[-3] = listaAntiga[2]
    listaSenha[2] = listaAntiga[-3]

    # Troca os números pelos caracteres...
    for i in range (tamanhoSenha):
        if listaSenha[i] =="W":
            listaSenha[i] = "0"
        elif listaSenha[i] == "#":
            listaSenha[i] = "1"
        elif listaSenha[i] == "Z":
            listaSenha[i] = "2"
        elif listaSenha[i] == "%":
            listaSenha[i] = "3" 
        elif listaSenha[i] == "X":
            listaSenha[i] = "4"
        elif listaSenha[i] == "@":
            listaSenha[i] = "5"
        elif listaSenha[i] == "&":
            listaSenha[i] = "6"
        elif listaSenha[i] == "k":
            listaSenha[i] = "7"
        elif listaSenha[i] == "H":
            listaSenha[i] = "8"
        elif listaSenha[i] == "?":
            listaSenha[i] = "9"
    
    
    print (f"Sua senha desencriptografada é: {listaSenha}")
    print(listaAntiga)

desencriptar()