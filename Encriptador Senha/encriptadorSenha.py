def encriptar():
    senha = input("Digite sua senha numérica para ENCRIPTAR...")
    listaSenha = []
    for letra in senha:
        listaSenha.append(letra)

    tamanhoSenha = len(senha)
    
    # Troca os números pelos caracteres...
    for i in range (tamanhoSenha):
        if listaSenha[i] =="0":
            listaSenha[i] = "W"
        elif listaSenha[i] == "1":
            listaSenha[i] = "#"
        elif listaSenha[i] == "2":
            listaSenha[i] = "Z"
        elif listaSenha[i] == "3":
            listaSenha[i] = "%" 
        elif listaSenha[i] == "4":
            listaSenha[i] = "X"
        elif listaSenha[i] == "5":
            listaSenha[i] = "@"
        elif listaSenha[i] == "6":
            listaSenha[i] = "&"
        elif listaSenha[i] == "7":
            listaSenha[i] = "K"
        elif listaSenha[i] == "8":
            listaSenha[i] = "H"
        elif listaSenha[i] == "9":
            listaSenha[i] = "?"
    
    # Embaralha alguns caracteres
    listaAntiga  = list(listaSenha)
    listaSenha[0] = listaAntiga[-1]
    listaSenha[-1] = listaAntiga[0]
    listaSenha[2] = listaAntiga[-3]
    listaSenha[-3] = listaAntiga[2]
    
    print (f"Sua senha encriptografada é: {listaSenha}")

encriptar()