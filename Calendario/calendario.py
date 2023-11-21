from tkinter import *
import calendar

def iniciarCalendario():
    nova_janela = Tk()
    nova_janela.config(background="black")
    nova_janela.title("Calendario")
    nova_janela.geometry("545x575")
    fetch_year = int(year_field.get())
    cal_content = calendar.calendar(fetch_year)
    cal_year = Label(nova_janela, text=cal_content, font=("Consolas", 10 ,"bold"))
    cal_year.grid(row=5, column=1, padx=20)
    nova_janela.mainloop()

if __name__ == "__main__":
    janela = Tk()
    janela.config(background="black")
    janela.title("Calendário Python - CGS")
    janela.geometry("300x190")
    cal = Label(janela, text="Calendário", bg="dark gray", font=("comic sans", 43, "bold"))
    year = Label(janela, text="Digite o ano desejado abaixo:", bg="green", font=40)
    year_field = Entry(janela, font=20)
    Show = Button(janela, text="Iniciar Calendário", fg="black", bg="green", font=30, command=iniciarCalendario)
    Exit = Button(janela, text="Sair", fg="black", bg="green", font=20, command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=2, column=1)
    year_field.grid(row=3, column=1)
    Show.grid(row=4, column=1)
    Exit.grid(row=6, column=1)
   
    janela.mainloop()
   




