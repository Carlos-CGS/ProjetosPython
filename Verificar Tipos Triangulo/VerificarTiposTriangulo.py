# Verificador dos tipos de triângulo

ladoA = eval(input("Digite o tamanho do primeiro lado: "))
ladoB = eval(input("Digite o tamanho do segundo lado: "))
ladoC =  eval(input("Digite o tamanho do terceiro lado: "))

maiorLado = max(ladoA, ladoB, ladoC)

if maiorLado < (ladoA + ladoB + ladoC) - maiorLado:
    print("Os lados formam um triangulo!")

    if ladoA == ladoB and ladoB == ladoC and ladoC == ladoA:
        print("Este é um triangulo Equilátero - (Todos os lado iguais.)")
    elif ladoA != ladoB and ladoB != ladoC and ladoC != ladoA:
        print("Este triangulo é Escaleno - (Todos os lados diferentes.)")
    else:
        print("Este triangulo é Isósceles - (Dois lados iguais e um diferente.)")
else:
    ("Os lados não formam um triangulo!")  