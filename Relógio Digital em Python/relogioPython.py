from tkinter import *
from time import strftime

# Criar Função Atualizar o Relógio
def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text = horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

# Criação Janela Principal
janela = Tk()
janela.title("Relógio Digital Python")

# Definição do Rótulo para exibir o relógio
rotulo_relogio = Label(
    janela,
    font = ("Comic Sans", 30, "bold"),
    background = "light green",
    foreground = "black"
)

# Posicionamento do relógio na tela
rotulo_relogio.pack(anchor = "center")

# Inicia a atulização do Relógio
atualizar_relogio()

# Inicia o Loop principal da Interface
janela.mainloop()