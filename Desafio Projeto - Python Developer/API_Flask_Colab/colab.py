# !pip install flask flask-ngrok

from flask import Flask, jsonify
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)  # Inicializa o ngrok quando a aplicação começa

# Dados JSON simples
data = [
    {"id": 1, "nome": "Alice", "idade": 30, "cidade": "São Paulo", "pais": "Brasil"},
    {"id": 2, "nome": "Bob", "idade": 25, "cidade": "Rio de Janeiro", "pais": "Brasil"},
    {"id": 3, "nome": "Charlie", "idade": 35, "cidade": "Curitiba", "pais": "Brasil"}
]

@app.route('/index')
def index():
    return jsonify(data)

@app.route('/')
def home():
    return "Hello World!"

if __name__ == '__main__':
    app.run()