import random

senha = ""
caracteresLetra = "qwertyuiopasdfghjklçzxcvbnm"
caracteresNumero = "0123456789"
caracteresEspecial = "!@#$%&*?*"
for digito in range (4):
    aleatorio1 = random.choice(caracteresLetra)
    senha += aleatorio1
for digito in range (2):
    aleatorio2 = random.choice(caracteresNumero)
    senha += aleatorio2
for digito in range (2):
    aleatorio3 = random.choice(caracteresEspecial)
    senha += aleatorio3

print("Senha nova gerada: " + senha)
