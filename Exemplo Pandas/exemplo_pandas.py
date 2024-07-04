import pandas as pd

# Carregar a base de dados do arquivo CSV
df = pd.read_csv('Python/Pandas/vendas.csv')

# Exibir os primeiros registros
print("Primeiros registros:")
print(df.head())

# Exibir informações gerais sobre o DataFrame
print("\nInformações gerais:")
print(df.info())

# Calcular o valor total de cada venda (Quantidade * Preço Unitário)
df['Valor Total'] = df['Quantidade'] * df['Preço Unitário']

# Exibir o DataFrame com a nova coluna
print("\nDataFrame com a coluna 'Valor Total':")
print(df)

# Calcular o total de vendas
total_vendas = df['Valor Total'].sum()
print(f"\nTotal de vendas: R$ {total_vendas:.2f}")

# Agrupar por Produto e somar as quantidades e valores
resumo_produtos = df.groupby('Produto').agg({
    'Quantidade': 'sum',
    'Valor Total': 'sum'
}).reset_index()

# Exibir o resumo por produto
print("\nResumo de vendas por produto:")
print(resumo_produtos)

# Filtrar vendas acima de R$ 1000,00
vendas_acima_1000 = df[df['Valor Total'] > 1000.00]
print("\nVendas acima de R$ 1000,00:")
print(vendas_acima_1000)

# Salvar o resumo por produto em um novo arquivo CSV
resumo_produtos.to_csv('resumo_produtos.csv', index=False)
print("\nResumo por produto salvo em 'resumo_produtos.csv'.")
