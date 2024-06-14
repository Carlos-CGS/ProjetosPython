class ModeloIA:
    def __init__(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades
    
    def __str__(self):
        return self.nome

# TODO: Crie uma função que recebe as características desejadas e recomenda um modelo de IA com base nelas:   
# TODO: Crie uma lista de 'ModeloIA' com suas características pontuadas na descrição:
def recomendar_modelo(caracteristicas):
    modelos = [
        ModeloIA("Claude 3 Opus", 9, 10, 5, ["Pesquisa", "Desenvolvimento Acelerado"]),
        ModeloIA("Claude 3 Sonnet", 8, 5, 7, ["Codificação", "Recuperação de informações"]),
        ModeloIA("Claude 3 Haiku", 7, 9, 6, ["Velocidade", "Resumo de dados não estruturados"])
    ]

    modelo_recomendado = None
  # Aqui é convertido as capacidades inseridas pelo usuário para minúsculas:
    capacidades_usuario = [capacidade.lower() for capacidade in caracteristicas['Capacidades']]

    for modelo in modelos:
        # Convertemos as capacidades do modelo para minúsculas:
        capacidades_modelo = [capacidade.lower() for capacidade in modelo.capacidades]
        
        if all(capacidade in capacidades_usuario for capacidade in capacidades_modelo):
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo

    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."

# Aqui temos a função que gera uma explicação para o modelo recomendado:
def gerar_explicacao(modelo, caracteristicas):
    if isinstance(modelo, ModeloIA):
        explicacao = f"O {modelo.nome} é o modelo recomendado."
        return explicacao
    else:
        return modelo

# Aqui fica a função que solicita características desejadas ao usuário:
def obter_caracteristicas():
    caracteristicas = {}
    caracteristicas['Desempenho'] = int(input())
    caracteristicas['Velocidade'] = int(input())
    caracteristicas['Custo'] = int(input())
    capacidades = input().split(',')
    caracteristicas['Capacidades'] = [capacidade.strip() for capacidade in capacidades]
    return caracteristicas

caracteristicas_entrada = obter_caracteristicas()
melhor_modelo = recomendar_modelo(caracteristicas_entrada)
explicacao = gerar_explicacao(melhor_modelo, caracteristicas_entrada)

print(explicacao)