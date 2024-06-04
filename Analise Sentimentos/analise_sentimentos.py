import re

def analise_sentimento(comentario):
    # Divisão do comentário em palavras
    palavras = re.findall(r'\b\w+\b', comentario.lower())
    
    # Lista de palavras positivas, negativas e neutras
    positivas = ["bom", "boa", "ótimo", "excelente", "maravilhoso", "gostei", "incrível", "amei", "amo", "incrivel", "fantástico", "feliz","alegre"]
    negativas = ["ruim", "péssimo", "horrível", "terrível", "odeio", "triste", "chateado", "lamentável"]
    neutras = ["mas", "deixou", "apesar", "embora", "mediano", "apenas", "contudo"]

    # Contagem de palavras positivas, negativas e neutras
    count_positivo = sum(palavra in positivas for palavra in palavras)
    count_negativo = sum(palavra in negativas for palavra in palavras)
    count_neutro = sum(palavra in neutras for palavra in palavras)

    # Verifica se há mais palavras positivas do que negativas no comentário e se não há palavras neutras. Se essa condição for verdadeira, o comentário é considerado positivo.
    if count_positivo > count_negativo and count_neutro == 0:
        return "Positivo"
    elif count_negativo > count_positivo and count_neutro == 0:
        return "Negativo"
    else:
        return "Neutro"

if __name__ == "__main__":
    comentario = input("Insira sua mensagem...")
    sentimento = analise_sentimento(comentario)
    print("Sentimento:", sentimento)
