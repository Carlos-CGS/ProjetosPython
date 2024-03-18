# Encriptador e Desencriptador de Senhas Numéricas em Python

### Proposta de um encriptador e desencriptador de senha básico em python que criei do zero para enviar senhas de "forma mais segura" pela rede:

# Código Encriptador:
- Solicito ao usuário que insira uma senha numérica e tranformo a string informada em uma lista através de um ```for letra in senha:``` junto da função ```listaSenha.append(letra)```;
- Após verififico a quantidade de carácter na senha através da função ```len(senha)``` e adicono a variável ```tamanhoSenha```;
- Logo após utilizo outro for:```for i in range (tamanhoSenha):``` para trocar cada numero inserido pelo caracter correspondente, utilizando como contador o tamanho da senha ```tamanhoSenha```;
- Para finalizar troco o valor do ```índice 0``` pelo valor do ```índice -1``` e o valor do ```índice 2``` pelo valor do ```íncide -3```, utilizando a variável ```listaAntiga``` como apoio.
- Ao final imprimo a senha criptografada.

# Código Desencriptador:
- Solicito ao usuário que insira a senha criptografada e tranformo a string informada em uma lista através de um ```for letra in senha:``` junto da função ```listaSenha.append(letra)```;
- Ao contrário do encriptador, aqui começo desembaralhando a ordem dos carácteres, trocando o valor do ```índice -1``` pelo valor do ```índice 0``` e o valor do ```índice -3``` pelo valor do ```íncide 2```, novamente utilizando a variável ```listaAntiga``` como apoio;
- Para finalizar utilizo outro for:```for i in range (tamanhoSenha):``` para trocar cada caractere inserido pelo numero correspondente, utilizando como contador o tamanho da senha ```tamanhoSenha```;
- E finalizo imprimindo a nova senha desencriptografada;
