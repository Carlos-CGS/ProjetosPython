# Desafio: Cálculo de Métricas de Avaliação de Aprendizado - DIO

Neste projeto, vamos calcular as principais métricas para avaliação de modelos de classificação de dados: **acurácia**, **sensibilidade (recall)**, **especificidade**, **precisão** e **F-score**.

## Definições das Métricas

Para calcular as métricas, precisamos da **matriz de confusão**, que nos fornece os seguintes valores:

- **VP**: Verdadeiros Positivos
- **VN**: Verdadeiros Negativos
- **FP**: Falsos Positivos
- **FN**: Falsos Negativos

## Fórmulas das Métricas

# Cálculo das Métricas de Avaliação

Vamos calcular as métricas de avaliação usando uma matriz de confusão exemplo:

|                   | Predito Positivo | Predito Negativo |
| ----------------- | ---------------- | ---------------- |
| **Real Positivo** | VP = 50          | FN = 10          |
| **Real Negativo** | FP = 5           | VN = 35          |

## Fórmulas das Métricas

```python
# Fórmula: Acurácia = (VP + VN) / (VP + VN + FP + FN)
acuracia = (VP + VN) / (VP + VN + FP + FN)
print(f"Acurácia: {acuracia:.2f}")
Acurácia: 0.85

# Fórmula: Precisão = VP / (VP + FP)
precisao = VP / (VP + FP)
print(f"Precisão: {precisao:.3f}")
Precisão: 0.909

# Fórmula: Sensibilidade = VP / (VP + FN)
sensibilidade = VP / (VP + FN)
print(f"Sensibilidade: {sensibilidade:.3f}")
Sensibilidade: 0.833

# Fórmula: Especificidade = VN / (VN + FP)
especificidade = VN / (VN + FP)
print(f"Especificidade: {especificidade:.3f}")
Especificidade: 0.875

# Fórmula: F-score = 2 * (Precisão * Sensibilidade) / (Precisão + Sensibilidade)
f_score = 2 * (precisao * sensibilidade) / (precisao + sensibilidade)
print(f"F-score: {f_score:.3f}")
F-score: 0.869
```

## Conclusão

Essas métricas podem ser adaptadas para diferentes cenários e usadas para ajustar e melhorar os modelos de aprendizado de máquina.
