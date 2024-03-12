# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.lower() == "sim"
    afinidade_animais = afinidade_animais.lower() == "sim"

    # Desenvolva a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    elif intensidade >= 7 and  componente_raro == True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais == False:
      return "A afinidade elemental do feiticeiro é com o elemento Água!"
    elif intensidade >= 7 and componente_raro == True and fase_lunar == "cheia" and idade_feiticeiro <= 100 and afinidade_animais == True:
      return "A afinidade elemental do feiticeiro é com o elemento Terra!"
    else:
      return "A afinidade elemental do feiticeiro é com o elemento Ar!"
   

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão
print(resultado)