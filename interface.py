import requests
from tkinter import *

def soma_numero():
    try:
        num1 = int(entry1.get())
        num2 = int(entry2.get())
        total = num1 + num2
        resultado_label.config(text=f"Total: {total}")
    except ValueError:
        resultado_label.config(text="Por favor, insira números válidos.")


janela = Tk()
janela.title("Soma")

texto = Label(janela, text="Soma de números")
texto.grid(column=0, row=0, padx=10, pady=10)


entry1 = Entry(janela)
entry1.grid(column=0, row=1, padx=10, pady=5)

entry2 = Entry(janela)
entry2.grid(column=1, row=1, padx=10, pady=5)


botao = Button(janela, text="Soma", command=soma_numero)
botao.grid(column=0, row=2, padx=10, pady=10)


resultado_label = Label(janela, text="")
resultado_label.grid(column=0, row=3, columnspan=2)

janela.mainloop()
