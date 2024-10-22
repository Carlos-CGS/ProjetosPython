import hashlib
import os
import tkinter as tk
from tkinter import filedialog, scrolledtext


def selecionar_primeiro_arquivo():
    global primeiro_arquivo
    primeiro_arquivo = filedialog.askopenfilename()
    if primeiro_arquivo:
        nome_primeiro_arquivo.set(os.path.basename(primeiro_arquivo))


def selecionar_segundo_arquivo():
    global segundo_arquivo
    segundo_arquivo = filedialog.askopenfilename()
    if segundo_arquivo:
        nome_segundo_arquivo.set(os.path.basename(segundo_arquivo))


def comparar_hashes():
    if not primeiro_arquivo or not segundo_arquivo:
        resultado_texto.insert(tk.END, "Selecione ambos os arquivos.\n")
        return

    hash1 = hashlib.new("ripemd160")
    hash1.update(open(primeiro_arquivo, "rb").read())

    hash2 = hashlib.new("ripemd160")
    hash2.update(open(segundo_arquivo, "rb").read())

    nome1 = os.path.basename(primeiro_arquivo)
    nome2 = os.path.basename(segundo_arquivo)

    if hash1.digest() != hash2.digest():
        resultado_texto.insert(
            tk.END, f"O arquivo {nome1} é diferente do arquivo {nome2}.\n"
        )
        resultado_texto.insert(tk.END, f"O Hash do {nome1} é: {hash1.hexdigest()}\n")
        resultado_texto.insert(tk.END, f"O Hash do {nome2} é: {hash2.hexdigest()}\n")
    else:
        resultado_texto.insert(
            tk.END, f"O arquivo {nome1} é igual ao arquivo {nome2}.\n"
        )
        resultado_texto.insert(tk.END, f"O Hash do {nome1} é: {hash1.hexdigest()}\n")
        resultado_texto.insert(tk.END, f"O Hash do {nome2} é: {hash2.hexdigest()}\n")


# Inicialização da interface
root = tk.Tk()
root.title("Comparador de Hashes - CGS")
root.configure(bg="darkgreen")

primeiro_arquivo = ""
segundo_arquivo = ""

# Variáveis para os nomes dos arquivos
nome_primeiro_arquivo = tk.StringVar()
nome_segundo_arquivo = tk.StringVar()

# Botões e labels
tk.Label(root, text="Primeiro Arquivo:", bg="darkgreen", fg="white").pack(pady=5)
tk.Entry(
    root, textvariable=nome_primeiro_arquivo, state="readonly", bg="lightgreen"
).pack(pady=5)
tk.Button(
    root,
    text="Selecionar Primeiro Arquivo",
    command=selecionar_primeiro_arquivo,
    bg="green",
    fg="white",
).pack(pady=5)

tk.Label(root, text="Segundo Arquivo:", bg="darkgreen", fg="white").pack(pady=5)
tk.Entry(
    root, textvariable=nome_segundo_arquivo, state="readonly", bg="lightgreen"
).pack(pady=5)
tk.Button(
    root,
    text="Selecionar Segundo Arquivo",
    command=selecionar_segundo_arquivo,
    bg="green",
    fg="white",
).pack(pady=5)

tk.Button(
    root, text="Comparar Hashes", command=comparar_hashes, bg="green", fg="white"
).pack(pady=10)

# Campo de texto para os resultados
resultado_texto = scrolledtext.ScrolledText(
    root, wrap=tk.WORD, width=50, height=10, bg="lightgreen"
)
resultado_texto.pack(pady=10)

root.mainloop()
