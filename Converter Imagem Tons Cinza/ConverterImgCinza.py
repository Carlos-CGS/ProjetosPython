from PIL import Image
import os


# Função para carregar a imagem PNG
def carregar_imagem(caminho):
    return Image.open(caminho)


# Função para converter a imagem para tons de cinza
def converter_para_cinza(imagem):
    return imagem.convert("L")  # Converte para escala de cinza (L)


# Função para converter a imagem para preto e branco
def converter_para_pb(imagem, limiar=128):
    imagem_cinza = imagem.convert("L")  # Converte para tons de cinza
    imagem_pb = imagem_cinza.point(lambda p: p > limiar and 255)  # Limiar para PB
    return imagem_pb


# Fluxo principal
if __name__ == "__main__":
    print("Certifique-se de que o arquivo PNG está na mesma pasta do script.")

    # Obter o diretório do script
    pasta_raiz = os.path.dirname(os.path.abspath(__file__))
    print(f"Pasta raiz do script: {pasta_raiz}")

    # Solicitar o nome do arquivo ao usuário
    caminho_imagem = input("Digite o nome do arquivo PNG (incluindo extensão): ")

    # Construir o caminho completo
    caminho_completo = os.path.join(pasta_raiz, caminho_imagem)

    # Verificar se o arquivo existe
    if not os.path.exists(caminho_completo):
        print(
            f"Erro: O arquivo '{caminho_imagem}' não foi encontrado na pasta '{pasta_raiz}'."
        )
    else:
        # Carregar a imagem PNG
        imagem = carregar_imagem(caminho_completo)
        print(f"Imagem '{caminho_imagem}' carregada com sucesso!")

        # Converter para tons de cinza e salvar
        imagem_cinza = converter_para_cinza(imagem)
        caminho_saida_cinza = os.path.join(pasta_raiz, "imagem_tons_cinza.png")
        imagem_cinza.save(caminho_saida_cinza)
        print(f"Imagem em tons de cinza salva como '{caminho_saida_cinza}'.")

        # Converter para preto e branco e salvar
        imagem_pb = converter_para_pb(imagem)
        caminho_saida_pb = os.path.join(pasta_raiz, "imagem_preto_branco.png")
        imagem_pb.save(caminho_saida_pb)
        print(f"Imagem em preto e branco salva como '{caminho_saida_pb}'.")
