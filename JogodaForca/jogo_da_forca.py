import random

def escolher_palavra():
    palavras = ["python", "javascript", "frontend", "backend", "java"]
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 5
    ponto = 100

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra secreta.")

    while True:
        palavra_secreta = ""
        for letra in palavra:
            if letra in letras_corretas:
                palavra_secreta += letra
            else:
                palavra_secreta += "_"

        print(palavra_secreta)
        print("")

        if palavra_secreta == palavra:
            print(f"Parabéns! Você acertou a palavra ({palavra}) com {ponto} pontos.")
            break

        tentativa = input("Digite uma letra: ").lower()

        if tentativa in palavra:
            print("Letra correta!")
            letras_corretas.append(tentativa)
        else:
            print("Letra errada! Tente novamente.")
            letras_erradas.append(tentativa)
            tentativas -= 1 
            ponto -= 10
            print(f"Você tem {tentativas} tentativas restantes.")

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

if __name__ == "__main__":
    jogar_forca()