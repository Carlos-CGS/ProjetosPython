# Documentação do Código - Desafio DIO - Formação Python

Este projeto consiste em um desafio de código proposto pela Digital Innovation One (DIO), como parte do curso de Formação Python. O objetivo do desafio é integrar uma aplicação utilizando SQLAlchemy para interagir com um banco de dados relacional SQLite, e também utilizar Pymongo para interagir com um banco de dados NoSQL MongoDB.

## Estrutura do Projeto

O projeto é estruturado da seguinte forma:

- **SQLAlchemy.py**: Contém o código Python que utiliza SQLAlchemy para definir um esquema relacional com duas entidades (Cliente e Conta), criar as tabelas correspondentes no SQLite, inserir dados de exemplo e realizar operações de consulta.

- **Pymongo.py**: Demonstração de como adaptar o esquema relacional para um ambiente NoSQL com MongoDB usando Pymongo. Inclui a conexão ao MongoDB Atlas, a definição de documentos e a realização de operações de inserção e consulta.

## Funcionalidades Implementadas

### SQLAlchemy.py

1. **Definição de Tabelas com SQLAlchemy:**
   - Classe `Cliente` e `Conta` com campos como nome, CPF, endereço, tipo de conta, agência, número e valor.

2. **Operações de Banco de Dados:**
   - Criação das tabelas no SQLite.
   - Inserção de dados de exemplo usando sessões do SQLAlchemy.
   - Recuperação de dados usando consultas SQL-like.

3. **Exemplos de Consultas Realizadas:**
   - Recuperação de clientes por nome.
   - Recuperação de contas associadas a um cliente específico.
   - Ordenação de clientes por sobrenome.
   - Consulta com join entre `Cliente` e `Conta`.
   - Contagem total de instâncias em `Cliente`.

### Pymongo.py

1. **Conexão com MongoDB Atlas:**
   - Utilização da string de conexão do MongoDB Atlas para conectar à base de dados.

2. **Definição e Inserção de Documentos:**
   - Estruturação de documentos para representar clientes e suas contas.
   - Inserção de documentos na coleção `bank` do MongoDB.

3. **Operações de Consulta:**
   - Recuperação de clientes por nome.
   - Projeção de contas associadas a um cliente específico.
   - Ordenação de clientes por nome.
   - Contagem total de documentos na coleção `bank`.

## Execução e Requisitos

Para executar este projeto, são necessários:

- Python 3.x
- Bibliotecas SQLAlchemy e Pymongo instaladas (`pip install sqlalchemy pymongo`)

Certifique-se de configurar corretamente as strings de conexão para o SQLite e MongoDB Atlas conforme necessário no código.

---

Este projeto foi desenvolvido como parte do desafio proposto pela DIO Digital Innovation One no curso de Formação Python. Ele serve como uma introdução prática ao uso de bancos de dados relacionais e NoSQL com Python, usando SQLAlchemy e Pymongo para integração com SQLite e MongoDB, respectivamente.
