# J.A.R.V.I.S.
# Exemplo de algoritmo de Processamento de Linguagem Natural
# pip install speechRecognition
# pip install pyaudio
# pip install pyttsx3
import speech_recognition as sr
import os
import pyttsx3

# Inicializar o Engine de Síntese de Fala
engine = pyttsx3.init()

def falar(texto):
    #Faz o Computador Falar
    engine.say(texto)
    engine.runAndWait()

def apresentacao():
    #Apresentação
    print("Iniciando o Sistema. Sistema 100% carregado e operando. Me chamo Jarvis.")
    falar("Iniciando o Sistema. Sistema 100% carregado e operando. Me chamo Jarvis.")

# Função para Ouvir e Reconhecer Fala:
def ouvir_microfone():
    # Habilita Microfone Usuário
    microfone = sr.Recognizer()

    # Usando o Microfone
    with sr.Microphone() as source:
        # Chama um Algoritmo de Redução de Ruídos no som
        microfone.adjust_for_ambient_noise(source)

        # Frase para o Usuário Dizer Algo
        print("Como posso te ajudar?")
        falar("Como posso te ajudar?")
         
        # Armazena o que foi Dito em uma Variável
        audio = microfone.listen(source)

    try:
        # Passa a Variável para o Algoritmo Reconhecer os Padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        if "Jarvis navegador" in frase:
            os.system("start chrome.exe")
            falar("Abrindo o navegador")
            return False
        elif "Jarvis calculadora" in frase:
            os.system("start calc.exe")
            falar("Abrindo a calculadora")
            return False
        elif "Jarvis Paint" in frase:
            os.system("start mspaint.exe")
            falar("Abrindo o Paint")
            return False
        elif "Jarvis bloco de notas" in frase:
            os.system("start notepad.exe")
            falar("Abrindo o bloco de notas")
            return False
        elif "Jarvis Excel" in frase:
            os.system("start Excel.exe")
            falar("Abrindo o Excel")
            return False
        elif "Jarvis Word" in frase:
            os.system("start winword.exe")
            falar("Abrindo o Word")
            return False
        elif "Jarvis acessar CMD" in frase:
            os.system("start cmd.exe")
            falar("Abrindo o prompt de comando")
            return False
        elif "Jarvis desligar" in frase:
            falar("Desligando o sistema. Até logo.")
            os.system("exit")
            return True
        else:
            falar(f"O Comando {frase} não foi reconhecido, por favor tente novamente.")
            return False

    except sr.UnknownValueError:
        print("Não entendi, repita o que deseja.")

# Loop de Execução do Programa        
apresentacao()
while True:
    if ouvir_microfone():
        break