import re
import tkinter as tk
from tkinter import messagebox


def verificar_bandeira(cartao_numero):
    bandeiras = {
        "Visa": r"^4[0-9]{12}(?:[0-9]{3})?$",
        "MasterCard": r"^5[1-5][0-9]{14}$",
        "American Express": r"^3[47][0-9]{13}$",
        "Diners Club": r"^3(?:0[0-5]|[68][0-9])[0-9]{11}$",
        "Discover": r"^6(?:011|5[0-9]{2})[0-9]{12}$",
        "JCB": r"^(?:2131|1800|35\d{3})\d{11}$",
    }

    for bandeira, padrao in bandeiras.items():
        if re.match(padrao, cartao_numero):
            return bandeira
    return "Bandeira desconhecida"


def verificar_bandeira_gui():
    numero_cartao = entry.get()
    numero_cartao = re.sub(
        r"\D", "", numero_cartao
    )  # Remove todos os caracteres não numéricos
    bandeira = verificar_bandeira(numero_cartao)
    resultado_label.config(text=f"A bandeira do cartão é: {bandeira}")


# Configuração da interface gráfica
root = tk.Tk()
root.title("Verificador de Bandeira de Cartão - CGS")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Digite o número do cartão de crédito:").pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=5)

tk.Button(root, text="Verificar Bandeira", command=verificar_bandeira_gui).pack(pady=20)

resultado_label = tk.Label(root, text="")
resultado_label.pack(pady=10)

root.mainloop()
