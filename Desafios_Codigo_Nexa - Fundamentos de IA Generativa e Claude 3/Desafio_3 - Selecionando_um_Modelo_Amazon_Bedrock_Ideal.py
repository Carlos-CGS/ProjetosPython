modelos_disponiveis = [
  {"nome":"Claude 3 Opus", "pontuacao_desempenho":9, "preco_mensal":600},
  {"nome":"Claude 3 Sonnet", "pontuacao_desempenho":8, "preco_mensal":450},
  {"nome":"Claude 3 Haiku", "pontuacao_desempenho":7, "preco_mensal":350},
] # TODO: Crie uma lista de dicionários representando os três modelos do Amazon Bedrock, com 'nome', 'pontuacao_desempenho' e 'preco_mensal' :

def recomendar_modelo(modelos, orcamento):
    if orcamento < 250:
      return None, "Seu orçamento é muito baixo para recomendar um modelo adequado."
# TODO: Defina a função 'recomendar_modelo' e seus dois parâmetros 'modelos' e 'orcamento':
# TODO: Verifique se o orçamento fornecido é suficiente. Se o orçamento for inferior a 250, implemente a resposta adequada:

    modelos_dentro_orcamento = [modelo for modelo in modelos if modelo['preco_mensal'] <= orcamento]

    # Caso nenhum modelo esteja dentro do orçamento
    if not modelos_dentro_orcamento:
        modelo_mais_proximo = min(modelos, key=lambda x: abs(x['preco_mensal'] - orcamento))
        return modelo_mais_proximo['nome'], "Este modelo está mais próximo do seu orçamento."

    # Caso todos os modelos estejam dentro do orçamento
    melhor_modelo = max(modelos_dentro_orcamento, key=lambda x: x['pontuacao_desempenho'])
    return melhor_modelo['nome'], "Melhor desempenho dentro do seu orçamento."

# Solicitar orçamento do usuário
orcamento_usuario = float(input())

# Chamada da função para recomendar o modelo
modelo_recomendado, motivo = recomendar_modelo(modelos_disponiveis, orcamento_usuario)

# Saída da recomendação
if modelo_recomendado:
    print(modelo_recomendado + ". " + motivo)
else:
    print(motivo)