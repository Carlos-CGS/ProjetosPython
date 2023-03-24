MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input('Digite sua Idade!'))

if idade >= MAIOR_IDADE:
    print('Voce pode inicar o processo para tirar CNH!')
else:
    print('Voce ainda não pode tirar sua CNH!')

if idade >= MAIOR_IDADE:
    print('Maior Idade, pode tirar sua CNH ! Processo prático e teórico iniciado')
elif idade == IDADE_ESPECIAL:
    print('Voce pode iniciar o processo teórico')
else:
    print('Voce ainda não pode iniciar o processo para obtenção da CNH!')