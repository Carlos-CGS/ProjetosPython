import pandas as pd

# Dados de entrada
dados_entrada = {
    'Nome': ['Carlos', 'José', 'Mário'],
    'ID': [1, 2, 3]
}

# Criação de um DataFrame a partir dos dados de entrada (Extract)
df = pd.DataFrame(dados_entrada)

# Etapa de Transformação (Transform)
df['Saudacao'] = 'Bem vindo ao BotCamp Santander Dev Week , ' + df['Nome']

# Etapa de Carregamento (Load)
df.to_excel('EntregaProjeto.xlsx', index=False)

# Exibir o DataFrame resultante
print(df)