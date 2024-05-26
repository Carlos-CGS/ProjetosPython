import speech_recognition as sr
import pyttsx3
import random

def ouvir_microfone():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        frase = recognizer.recognize_google(audio, language='pt-BR')
        return frase
    except sr.UnknownValueError:
        print("Não entendi o que você disse.")
        falar("Não entendi o que você disse.")
        return None

def falar(texto):
    engine = pyttsx3.init()
    engine.say(texto)
    engine.runAndWait()

def apresentacao():
    print("Adivinhe o número secreto de 1 a 100:")
    falar("Adivinhe o número secreto de 1 a 100:")

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        tentativa = ouvir_microfone()

        if tentativa:
            try:
                tentativa_numero = int(tentativa)
                tentativas += 1

                if tentativa_numero < numero_secreto:
                    print("O número secreto é maior.")
                    falar("O número secreto é maior.")
                elif tentativa_numero > numero_secreto:
                    print("O número secreto é menor.")
                    falar("O número secreto é menor.")
                else:
                    print(f"Parabéns! Você acertou o número secreto {numero_secreto} com {tentativas} tentativas.")
                    falar(f"Parabéns! Você acertou o número secreto {numero_secreto} com {tentativas} tentativas.")
                    break
            except ValueError:
                print("Por favor, diga um número válido.")
                falar("Por favor, diga um número válido.")

if __name__ == "__main__":
    apresentacao()
    jogo_adivinhacao()
