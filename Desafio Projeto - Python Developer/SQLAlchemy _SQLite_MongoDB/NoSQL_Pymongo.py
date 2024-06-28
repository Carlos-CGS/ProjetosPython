import pymongo
from pymongo import MongoClient

# Conectar ao MongoDB Atlas
client = MongoClient("mongodb+srv://Carlos-CGS:minh@Senha789456123@cluster0.syadbl3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["banco_dados"]
collection = db["bank"]

# Definir estrutura dos documentos
clientes = [
    {
        "nome": "Maria",
        "cpf": "123456789",
        "endereco": "Rua A, 123",
        "contas": [
            {"tipo": "Corrente", "agencia": 1, "numero": 123, "valor": 1000},
            {"tipo": "Poupança", "agencia": 1, "numero": 456, "valor": 500}
        ]
    },
    {
        "nome": "Joao",
        "cpf": "987654321",
        "endereco": "Avenida B, 456",
        "contas": [
            {"tipo": "Corrente", "agencia": 2, "numero": 789, "valor": 1500}
        ]
    },
    {
        "nome": "Ana",
        "cpf": "456789123",
        "endereco": "Rua C, 789",
        "contas": []
    }
]

# Inserir documentos
collection.insert_many(clientes)

# Recuperar e exibir documentos
print("Recuperando clientes:")
for cliente in collection.find({"nome": {"$in": ["Maria", "Joao"]}}):
    print(cliente)

print("\nRecuperando contas de Maria:")
for conta in collection.find({"nome": "Maria"}, {"contas": 1}):
    print(conta["contas"])

print("\nRecuperando todos os clientes ordenados por nome:")
for cliente in collection.find().sort("nome", pymongo.ASCENDING):
    print(cliente)

print("\nTotal de clientes:", collection.count_documents({}))
