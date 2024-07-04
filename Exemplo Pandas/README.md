# Documentação do Script `manipular_vendas.py`

## Descrição

Este script em Python utiliza a biblioteca `pandas` para realizar diversas operações de manipulação de dados em uma base de dados fictícia de vendas armazenada em um arquivo CSV. O script realiza as seguintes operações:

1. Carrega a base de dados de um arquivo CSV.
2. Exibe os primeiros registros da base de dados.
3. Exibe informações gerais sobre a base de dados.
4. Calcula o valor total de cada venda.
5. Calcula o total de vendas.
6. Agrupa os dados por produto e soma as quantidades e valores.
7. Filtra vendas cujo valor total é acima de R$ 1000,00.
8. Salva o resumo das vendas por produto em um novo arquivo CSV.

## Arquivo de Entrada

- `vendas.csv`: Arquivo CSV contendo os dados de vendas. O formato esperado do arquivo é o seguinte:

```csv
Data,Produto,Quantidade,Preço Unitário
2024-07-01,Notebook,2,3500.00
2024-07-01,Mouse,10,50.00
2024-07-02,Teclado,5,120.00
2024-07-02,Monitor,3,800.00
2024-07-03,Cadeira Gamer,1,1000.00
2024-07-03,Mousepad,15,30.00
