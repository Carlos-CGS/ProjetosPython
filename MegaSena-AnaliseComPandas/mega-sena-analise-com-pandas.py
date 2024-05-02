import pandas as pd

# Carregar o arquivo Excel
def carregar_arquivo_excel(nome_arquivo):
    try:
        planilha = pd.read_excel(nome_arquivo)
        return planilha
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho e tente novamente.")
        exit()

# Obter os seis números mais sorteados
def obter_seis_numeros_mais_sorteados(planilha):
    if planilha is not None:
        # Contar a frequência dos números
        frequencia_numeros = planilha.stack().value_counts()
        # Obter os seis números mais frequentes
        seis_mais_frequentes = frequencia_numeros.head(6)
        return seis_mais_frequentes
    else:
        return None

# Imprimir os seis números mais sorteados como em um jogo de Mega Sena
def imprimir_resultado_mega_sena(seis_mais_frequentes):
    if seis_mais_frequentes is not None:
        numeros_sorteados = sorted(seis_mais_frequentes.index)
        print("Resultado da Mega Sena:")
        print(", ".join(map(str, numeros_sorteados)))
    else:
        print("Não foi possível encontrar os números mais sorteados.")

if __name__ == "__main__":
    # Carregar o arquivo Excel
    nome_arquivo = 'Python\Probabilidade Real Numeros Sorteados\mega-sena.xlsx'  
    planilha = carregar_arquivo_excel(nome_arquivo)

    # Obter os seis números mais sorteados
    seis_mais_frequentes = obter_seis_numeros_mais_sorteados(planilha)

    # Imprimir o resultado da Mega Sena
    imprimir_resultado_mega_sena(seis_mais_frequentes)
